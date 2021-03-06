#
# This file is protected by Copyright. Please refer to the COPYRIGHT file
# distributed with this source distribution.
#
# This file is part of REDHAWK core.
#
# REDHAWK core is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# REDHAWK core is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.
#

import jinja2

from redhawk.codegen.jinja.ports import PortFactory

from generator import BuiltinPythonPort

class MessagePortFactory(PortFactory):
    REPID = 'IDL:ExtendedEvent/MessageEvent:1.0'

    def match(self, port):
        return (port.repid() == self.REPID)

    def generator(self, port):
        if port.isProvides():
            return MessageConsumerPortGenerator(port)
        else:
            return MessageSupplierPortGenerator(port)

class MessageConsumerPortGenerator(BuiltinPythonPort):
    def __init__(self, port):
        BuiltinPythonPort.__init__(self, 'ossie.events.MessageConsumerPort', port)

    def _ctorArgs(self, name):
        return ('thread_sleep=0.1',)

class MessageSupplierPortGenerator(BuiltinPythonPort):
    def __init__(self, port):
        BuiltinPythonPort.__init__(self, 'ossie.events.MessageSupplierPort', port)
