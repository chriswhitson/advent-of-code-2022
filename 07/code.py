def buildDirectoryStructure(outputs: list):    
    fileSizes = 0
    subDirs = []
    children = {}
    while len(outputs) > 0:     
        match outputs.pop(0).split():
            case ['$', 'cd', '..']:
                break
            case ['$', 'cd', directory]:
                children[directory] = buildDirectoryStructure(outputs)
            case ['$', _]:
                pass
            case ['dir', directory]:
                subDirs.append(directory)
                pass
            case [fileSize, _]:
                fileSizes += int(fileSize)
            
    return {
        'size': fileSizes + sum(x['size'] for x in children.values()),
        'children': children  
    }

def getSizes(f:dict):
    x = [k for c in f['children'].values() for k in getSizes(c)]
    if f['size'] < 100000:
        x.append(f['size'])
    return x

def getLargeSizes(f:dict, size, dirName=''):
    x = [c for k,v in f['children'].items() for c in getLargeSizes(v, size, k)]
    if f['size'] > size:
        x.append((dirName, f['size']))
    return x
  

with open('07/input.txt', 'r') as f:
    directoryStructure = buildDirectoryStructure(f.read().splitlines())

    # PART 1
    print(sum(getSizes(directoryStructure)))

    # Part 2
    totalSpace = 70_000_000 
    requiredSpace = 30_000_000
    unused = totalSpace - directoryStructure['size']
    deletionRequired = requiredSpace - unused
    print(min(a for _,a in getLargeSizes(directoryStructure, deletionRequired)))
