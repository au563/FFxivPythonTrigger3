from FFxivPythonTrigger import plugins
from FFxivPythonTrigger.saint_coinach import item_sheet


def create_message(container: int, slot: int, item_id: int):
    return {
        'action': 0x15b,
        'source': {
            'container': container,
            'slot': slot,
            'param3': 1,
            'param5': item_id,
        },
        'target': {
            'container': container,
            'slot': slot,
            'param3': 1,
            'param5': item_id,
        }
    }


messages = []
for item in plugins.XivMemory.inventory.get_item_in_containers_by_key(None, 'armoury_chest'):
    _item = item_sheet[item.item_id]
    if _item['EquipSlotCategory'].key and _item['Level{Equip}'] % 10:
        print(f'{item.container_id, item.idx} {_item["Name"]} ({_item["Level{Equip}"]})')
        plugins.XivNetwork.send_messages('zone', ('InventoryModifyHandler', create_message(item.container_id, item.idx, item.item_id)))

