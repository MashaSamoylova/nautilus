ctx.rule(u'START',u'var e;\n{NEW_OBJECT}')

ctx.rule(u'NEW_OBJECT',u'try \\{ {GLOBAL_OBJECT} } catch\\{e\\} \\{\\}\n {GLOBAL_OBJECT_PLAY}')
ctx.rule(u'NEW_OBJECT',u'try \\{ {GLOBAL_OBJECT} } catch\\{e\\} \\{\\}\n {GLOBAL_OBJECT_PLAY}\n{NEW_OBJECT}')

ctx.rule(u'NEW_OBJECT',u'try \\{ {TABLE_OBJECT} } catch\\{e\\} \\{\\}\n {TABLE_OBJECT_PLAY}')
ctx.rule(u'NEW_OBJECT',u'try \\{ {TABLE_OBJECT} } catch\\{e\\} \\{\\}\n {TABLE_OBJECT_PLAY}\n{NEW_OBJECT}')

ctx.rule(u'NEW_OBJECT',u'try \\{ {MEMORY_OBJECT} } catch\\{e\\} \\{\\}\n {MEMORY_OBJECT_PLAY}')
ctx.rule(u'NEW_OBJECT',u'try \\{ {MEMORY_OBJECT} } catch\\{e\\} \\{\\}\n {MEMORY_OBJECT_PLAY}\n{NEW_OBJECT}')

ctx.rule(u'NEW_OBJECT',u'try \\{ {MODULE_OBJECT} } catch\\{e\\} \\{\\}\n {MODULE_OBJECT_PLAY}')
ctx.rule(u'NEW_OBJECT',u'try \\{ {MODULE_OBJECT} } catch\\{e\\} \\{\\}\n {MODULE_OBJECT_PLAY}\n{NEW_OBJECT}')

ctx.rule(u'NEW_OBJECT',u'try \\{ {INSTANCE_OBJECT} } catch\\{e\\} \\{\\}\n {INSTANCE_OBJECT_PLAY}')
ctx.rule(u'NEW_OBJECT',u'try \\{ {INSTANCE_OBJECT} } catch\\{e\\} \\{\\}\n {INSTANCE_OBJECT_PLAY}\n{NEW_OBJECT}')

#####################################
# GLOBAL OBJECT
#####################################
ctx.rule(u'GLOBAL_OBJECT', u'var globalwasm = new WebAssembly.Global({GLOBAL_PARAMETERS});')

ctx.rule(u'GLOBAL_PARAMETERS', u'{GLOBAL_DESCRIPTOR_FLOAT}, {DECIMAL_NUMBER}')
ctx.rule(u'GLOBAL_PARAMETERS', u'{GLOBAL_DESCRIPTOR_INT}, {INTEGER}')
ctx.rule(u'GLOBAL_DESCRIPTOR_FLOAT', u'\\{value: {TYPE_FLOAT}, mutable: {BOOL} \\}')
ctx.rule(u'GLOBAL_DESCRIPTOR_INT', u'\\{value: {TYPE_INT}, mutable: {BOOL} \\}')

ctx.rule(u'GLOBAL_OBJECT_PLAY', u'try \\{ {GLOBAL_OBJECT_METHOD} \\} catch\\{e\\} \\{\\}\n{GLOBAL_OBJECT_PLAY}')
ctx.rule(u'GLOBAL_OBJECT_PLAY', u'try \\{ {GLOBAL_OBJECT_METHOD} \\} catch\\{e\\} \\{\\}')

ctx.rule(u'GLOBAL_OBJECT_METHOD', u'var number1 = globalwasm.value;')
ctx.rule(u'GLOBAL_OBJECT_METHOD', u'var number1 = globalwasm.valueOf();')
ctx.rule(u'GLOBAL_OBJECT_METHOD', u'var number1 = globalwasm.valueOf();')
ctx.rule(u'GLOBAL_OBJECT_METHOD', u'var string1 = globalwasm.toString();')
ctx.rule(u'GLOBAL_OBJECT_METHOD', u'globalwasm.value = {INTEGER};')

#####################################
# TABLE OBJECT
#####################################
ctx.rule(u'TABLE_OBJECT', u'var tablewasm = new WebAssembly.Table({TABLE_DESCRIPTOR});')

def generate_table_initial():
    import random
    return b"%d"%random.randint(0, 42)

def generate_table_maximum():
    import random
    return b"%d"%random.randint(43, 99)

ctx.rule(u'TABLE_DESCRIPTOR', u'\\{element: "anyfunc", initial: {TABLE_INITIAL} \\}')
ctx.rule(u'TABLE_DESCRIPTOR', u'\\{element: "anyfunc", initial: {TABLE_INITIAL},  maximum: {TABLE_MAXIMUM} \\}')

ctx.script(u'TABLE_INITIAL', [], generate_table_initial)
ctx.script(u'TABLE_MAXIMUM', [], generate_table_maximum)

ctx.rule(u'TABLE_OBJECT_PLAY', u'try \\{ {TABLE_OBJECT_METHOD} \\} catch\\{e\\} \\{\\}\n{TABLE_OBJECT_PLAY}')
ctx.rule(u'TABLE_OBJECT_PLAY', u'try \\{ {TABLE_OBJECT_METHOD} \\} catch\\{e\\} \\{\\}')

ctx.rule(u'TABLE_OBJECT_METHOD', u'var number2 = tablewasm.length - 1;')
ctx.rule(u'TABLE_OBJECT_METHOD', u'var funcRef = tablewasm.get({TABLE_INITIAL});')
ctx.rule(u'TABLE_OBJECT_METHOD', u'var number2 = tablewasm.grow({UNSIGNED_INTEGER});')
ctx.rule(u'TABLE_OBJECT_METHOD', u'tablewasm.set({TABLE_INITIAL}, {INTEGER});')

#####################################
# MEMORY OBJECT
#####################################
ctx.rule(u'MEMORY_OBJECT', u'var memorywasm = new WebAssembly.Memory({MEMORY_DESCRIPTOR});')

def generate_memory_initial():
    import random
    return b"%d"%random.randint(0, 9)

def generate_memory_maximum():
    import random
    return b"%d"%random.randint(9, 999)

ctx.rule(u'MEMORY_DESCRIPTOR', u'\\{ initial: {MEMORY_INITIAL} \\}')
ctx.rule(u'MEMORY_DESCRIPTOR', u'\\{ initial: {MEMORY_INITIAL},  maximum: {MEMORY_MAXIMUM} \\}')

ctx.script(u'MEMORY_INITIAL', [], generate_memory_initial)
ctx.script(u'MEMORY_MAXIMUM', [], generate_memory_maximum)

ctx.rule(u'MEMORY_OBJECT_PLAY', u'try \\{ {MEMORY_OBJECT_METHOD} \\} catch\\{e\\} \\{\\}\n{MEMORY_OBJECT_PLAY}')
ctx.rule(u'MEMORY_OBJECT_PLAY', u'try \\{ {MEMORY_OBJECT_METHOD} \\} catch\\{e\\} \\{\\}')

ctx.rule(u'MEMORY_OBJECT_METHOD', u'var number3 = memorywasm.buffer.length - 1;')
ctx.rule(u'MEMORY_OBJECT_METHOD', u'var array3 = memorywasm.buffer;')
ctx.rule(u'MEMORY_OBJECT_METHOD', u'var number3 = memorywasm.grow({UNSIGNED_INTEGER});')
ctx.rule(u'MEMORY_OBJECT_METHOD', u'memorywasm.buffer({MEMORY_INITIAL}) = {INTEGER};')
ctx.rule(u'MEMORY_OBJECT_METHOD', u'memorywasm.buffer({MEMORY_INITIAL}) = {UNSIGNED_INTEGER};')
ctx.rule(u'MEMORY_OBJECT_METHOD', u'for (var i = 0; i < memorywasm.buffer.length; i++) \\{memorywasm.buffer[i] = {UNSIGNED_INTEGER};\\}')

#####################################
# MODULE OBJECT
#####################################
ctx.rule(u'MODULE_OBJECT', u'var modulewasm = new WebAssembly.Module({BUFFER_SOURCE});')

# hello world module with main function exported
ctx.rule(u'BUFFER_SOURCE', u'new Uint8Array([0,97,115,109,1,0,0,0,1,133,128,128,128,0,1,96,0,1,127,3,130,128,128,128,0,1,0,4,132,128,128,128,0,1,112,0,0,5,131,128,128,128,0,1,0,1,6,129,128,128,128,0,0,7,145,128,128,128,0,2,6,109,101,109,111,114,121,2,0,4,109,97,105,110,0,0,10,138,128,128,128,0,1,132,128,128,128,0,0,65,42,11]);')

ctx.rule(u'MODULE_OBJECT_PLAY', u'try \\{ {MODULE_OBJECT_METHOD} \\} catch\\{e\\} \\{\\}\n{MODULE_OBJECT_PLAY}')
ctx.rule(u'MODULE_OBJECT_PLAY', u'try \\{ {MODULE_OBJECT_METHOD} \\} catch\\{e\\} \\{\\}')

ctx.rule(u'MODULE_OBJECT_METHOD', u'var array4 = WebAssembly.Module.customSections(modulewasm, {SECTION_NAME});')
ctx.rule(u'MODULE_OBJECT_METHOD', u'var array4 = WebAssembly.Module.exports(modulewasm);')
ctx.rule(u'MODULE_OBJECT_METHOD', u'var string4 = WebAssembly.Module.exports(modulewasm).toString();')
ctx.rule(u'MODULE_OBJECT_METHOD', u'var array4 = WebAssembly.Module.imports(modulewasm);')
ctx.rule(u'MODULE_OBJECT_METHOD', u'var string4 = WebAssembly.Module.imports(modulewasm).toString();')

ctx.rule(u'SECTION_NAME', u'name')
ctx.rule(u'SECTION_NAME', u'')
ctx.rule(u'SECTION_NAME', u'debug')
ctx.rule(u'SECTION_NAME', u'main')

#####################################
# INSTANCE OBJECT
#####################################
ctx.rule(u'INSTANCE_OBJECT', u'var instancewasm = new WebAssembly.Instance(modulewasm, {IMPORT_OBJECT}});')

ctx.rule(u'IMPORT_OBJECT', u'\\{\\}')
ctx.rule(u'IMPORT_OBJECT', u'\\{ js: \\{ globalwasm \\}\\}')
ctx.rule(u'IMPORT_OBJECT', u'\\{ js: \\{ tbl: tablewasm \\}\\}')
ctx.rule(u'IMPORT_OBJECT', u'\\{ js: \\{ mem: memorywasm \\}\\}')

ctx.rule(u'INSTANCE_OBJECT_PLAY', u'try \\{ {INSTANCE_OBJECT_METHOD} \\} catch\\{e\\} \\{\\}\n{INSTANCE_OBJECT_PLAY}')
ctx.rule(u'INSTANCE_OBJECT_PLAY', u'try \\{ {INSTANCE_OBJECT_METHOD} \\} catch\\{e\\} \\{\\}')

ctx.rule(u'INSTANCE_OBJECT_METHOD', u'instancewasm.exports.main();')
ctx.rule(u'INSTANCE_OBJECT_METHOD', u'memorywasm = instancewasm.exports.memory;')

#####################################
# HELPERS
#####################################
def generate_float():
    import random
    return b"%f"%random.uniform(-10000, +10000)

def generate_int():
    import random
    return b"%d"%random.randint(-10000, +10000)

def generate_uint():
    import random
    return b"%d"%random.randint(0, +10000)

ctx.script(u'DECIMAL_NUMBER', [], generate_float)
ctx.script(u'INTEGER', [], generate_int)
ctx.script(u'UNSIGNED_INTEGER', [], generate_uint)

ctx.rule(u'BOOL',u'true')
ctx.rule(u'BOOL',u'false')

ctx.rule(u'TYPE_FLOAT',u'f32')
ctx.rule(u'TYPE_FLOAT',u'f64')
ctx.rule(u'TYPE_INT', u'i32')
ctx.rule(u'TYPE_INT', u'i64')