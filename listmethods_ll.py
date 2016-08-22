# List all methods in an .net assembly using low level metadata access

from System.Reflection import MethodAttributes, MethodImplAttributes
import clr

def main():
	mod = dnlib.DotNet.ModuleDefMD.Load('ColorsDesktop.exe')
	ss = mod.Assembly.Modules[0].MetaData.StringsStream # Strings stream
	ts = mod.Assembly.Modules[0].MetaData.TablesStream # mod.Assembly.Modules[0].TablesStream

	print 'Listing Methods...'
	size = ts.MethodTable.Rows
	for i in xrange(1, size+1):
		row = ts.ReadMethodRow(i)
		if row.ImplFlags == int(MethodImplAttributes.IL): # Show only methods having CodeType IL
			print 'Name: {0}\tIsSpecial: {1}'.format(ss.Read(row.Name), int(MethodAttributes.SpecialName) & row.Flags != 0)


if __name__ == '__main__':
	try:
		clr.AddReferenceToFileAndPath('dnlib.dll')
		import dnlib
	except Exception, ex:
		print e
	else:
		main()
