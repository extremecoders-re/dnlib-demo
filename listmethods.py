# List all methods in an .net assembly
import clr

def main():
	mod = dnlib.DotNet.ModuleDefMD.Load('ColorsDesktop.exe')

	for mod in mod.Assembly.Modules:
		for typ in mod.Types:
			for method in typ.Methods:
				print 'Name: {0}\tIsSpecial: {1}'.format(method.Name, method.IsSpecialName)


if __name__ == '__main__':
	try:
		clr.AddReferenceToFileAndPath('dnlib.dll')
		import dnlib
	except Exception, ex:
		print e
	else:
		main()
