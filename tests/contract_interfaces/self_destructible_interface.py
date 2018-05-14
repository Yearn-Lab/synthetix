from tests.contract_interfaces.owned_interface import OwnedInterface
from utils.deployutils import mine_tx


class SelfDestructibleInterface(OwnedInterface):
    def __init__(self, contract, name):
        OwnedInterface.__init__(self, contract, name)
        self.contract = contract
        self.contract_name = name

        self.initiationTime = lambda: self.contract.functions.initiationTime().call()
        self.selfDestructBeneficiary = lambda: self.contract.functions.selfDestructBeneficiary().call()
        self.selfDestructDelay = lambda: self.contract.functions.selfDestructDelay().call()

        self.setBeneficiary = lambda sender, beneficiary: mine_tx(
            self.contract.functions.setBeneficiary(beneficiary).transact({'from': sender}), "setBeneficiary", self.contract_name)
        self.initiateSelfDestruct = lambda sender: mine_tx(
            self.contract.functions.initiateSelfDestruct().transact({'from': sender}), "initiateSelfDestruct", self.contract_name)
        self.terminateSelfDestruct = lambda sender: mine_tx(
            self.contract.functions.terminateSelfDestruct().transact({'from': sender}), "terminateSelfDestruct", self.contract_name)
        self.selfDestruct = lambda sender: mine_tx(
            self.contract.functions.selfDestruct().transact({'from': sender}), "selfDestruct", self.contract_name)
