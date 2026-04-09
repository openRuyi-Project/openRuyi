# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond deprecated 0

Name:           bluez
Version:        5.84
Release:        %autorelease
Summary:        Bluetooth tools and daemons
License:        GPL-2.0-or-later
URL:            http://www.bluez.org/
VCS:            git:https://git.kernel.org/pub/scm/bluetooth/bluez.git
#!RemoteAsset
Source:         https://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --enable-tools
BuildOption(conf):  --enable-library
BuildOption(conf):  --enable-external-ell
BuildOption(conf):  --disable-optimization
%if %{with deprecated}
BuildOption(conf):  --enable-deprecated
%endif
BuildOption(conf):  --enable-sixaxis
BuildOption(conf):  --enable-cups
BuildOption(conf):  --enable-nfc
BuildOption(conf):  --enable-mesh
BuildOption(conf):  --enable-hid2hci
BuildOption(conf):  --enable-testing
BuildOption(conf):  --enable-experimental
BuildOption(conf):  --enable-bap
BuildOption(conf):  --enable-bass
BuildOption(conf):  --enable-mcp
BuildOption(conf):  --enable-micp
BuildOption(conf):  --enable-csip
BuildOption(conf):  --enable-vcp
BuildOption(conf):  --with-systemdsystemunitdir=%{_unitdir}
BuildOption(conf):  --with-systemduserunitdir=%{_userunitdir}
BuildOption(conf):  --disable-manpages

BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libical)
BuildRequires:  make
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd
BuildRequires:  cups-devel
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ell)
BuildRequires:  systemd-rpm-macros

Requires:       dbus
%systemd_requires

%description
Utilities for use in Bluetooth applications. This is the main package containing
the core daemon and utilities.

%package        cups
Summary:        CUPS printer backend for Bluetooth printers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    cups
This package contains the CUPS backend for Bluetooth printers.

%if %{with deprecated}
%package        deprecated
Summary:        Deprecated Bluetooth applications
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    deprecated
Deprecated Bluetooth utilities like hciconfig, hcitool, etc.
%endif

%package        devel
Summary:        Development libraries for Bluetooth applications
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development libraries and headers for use in Bluetooth applications.

%package        hid2hci
Summary:        Put HID proxying bluetooth HCI's into HCI mode
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    hid2hci
Utility to switch supported Bluetooth devices into regular HCI mode.

%package        mesh
Summary:        Bluetooth mesh services
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    mesh
Services for Bluetooth mesh networking.

%package        obexd
Summary:        Object Exchange daemon for sharing content
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    obexd
Object Exchange daemon for sharing files, contacts etc over Bluetooth.

%conf -p
autoreconf -vif

%install -a

# "make install" fails to install gatttool, necessary for Bluetooth Low Energy
# Red Hat Bugzilla bug #1141909, Debian bug #720486
%if %{with deprecated}
install -m0755 attrib/gatttool %{buildroot}%{_bindir}
%endif

# "make install" fails to install avinfo
# Red Hat Bugzilla bug #1699680
install -m0755 tools/avinfo %{buildroot}%{_bindir}

# btmgmt is not installed by "make install", but it is useful for debugging
# some issues and to set the MAC address on HCIs which don't have their
# MAC address configured
install -m0755 tools/btmgmt %{buildroot}%{_bindir}

# Remove the cups backend from libdir, and install it in /usr/lib whatever the install
if test -d %{buildroot}/usr/lib64/cups ; then
   install -D -m0755 %{buildroot}/usr/lib64/cups/backend/bluetooth %{buildroot}%_cups_serverbin/backend/bluetooth
   rm -rf %{buildroot}%{_libdir}/cups
fi

rm -f ${RPM_BUILD_ROOT}/%{_sysconfdir}/udev/*.rules ${RPM_BUILD_ROOT}/usr/lib/udev/rules.d/*.rules
install -D -p -m0644 tools/hid2hci.rules %{buildroot}/%{_udevrulesdir}/97-hid2hci.rules
install -d -m0755 %{buildroot}/%{_localstatedir}/lib/bluetooth/mesh

#copy bluetooth config files
install -D -p -m0644 src/main.conf %{buildroot}/etc/bluetooth/main.conf
install -D -p -m0644 mesh/mesh-main.conf %{buildroot}/etc/bluetooth/mesh-main.conf
install -D -p -m0644 profiles/input/input.conf %{buildroot}/etc/bluetooth/input.conf
install -D -p -m0644 profiles/network/network.conf %{buildroot}/etc/bluetooth/network.conf
install -d -m 755 %{buildroot}%{_libexecdir}/bluetooth/

# Install the HCI emulator, useful for testing
install emulator/btvirt %{buildroot}/%{_libexecdir}/bluetooth/

%post
%systemd_post bluetooth.service

%preun
%systemd_preun bluetooth.service

%postun
%systemd_postun_with_restart bluetooth.service

%post hid2hci
/sbin/udevadm trigger --subsystem-match=usb

%post mesh
%systemd_user_post bluetooth-mesh.service

%preun mesh
%systemd_user_preun bluetooth-mesh.service

%post obexd
%systemd_user_post obex.service

%preun obexd
%systemd_user_preun obex.service

%files
%license COPYING
%doc AUTHORS ChangeLog
%attr(0555, root, root) %dir %{_sysconfdir}/bluetooth
%config(noreplace) %{_sysconfdir}/bluetooth/main.conf
%config(noreplace) %{_sysconfdir}/bluetooth/input.conf
%config(noreplace) %{_sysconfdir}/bluetooth/network.conf
%{_bindir}/avinfo
%{_bindir}/bluemoon
%{_bindir}/bluetoothctl
%{_bindir}/btattach
%{_bindir}/btmgmt
%{_bindir}/btmon
%{_bindir}/hex2hcd
%{_bindir}/mpris-proxy
%dir %{_libexecdir}/bluetooth
%{_libexecdir}/bluetooth/bluetoothd
%attr(0700, root, root) %dir %{_localstatedir}/lib/bluetooth
%dir %{_localstatedir}/lib/bluetooth/mesh
%{_datadir}/dbus-1/system.d/bluetooth.conf
%{_datadir}/dbus-1/system-services/org.bluez.service
%{_unitdir}/bluetooth.service
%{_userunitdir}/mpris-proxy.service
%{_datadir}/zsh/site-functions/_bluetoothctl
%{_libdir}/libbluetooth.so.*

%if %{with deprecated}
%files deprecated
%{_bindir}/ciptool
%{_bindir}/gatttool
%{_bindir}/hciattach
%{_bindir}/hciconfig
%{_bindir}/hcidump
%{_bindir}/hcitool
%{_bindir}/meshctl
%{_bindir}/rfcomm
%{_bindir}/sdptool
%endif

%files devel
%doc doc/*txt
%{_bindir}/isotest
%{_bindir}/l2test
%{_bindir}/l2ping
%{_bindir}/rctest
%{_libdir}/libbluetooth.so
%{_includedir}/bluetooth
%{_libdir}/pkgconfig/bluez.pc
%dir %{_libexecdir}/bluetooth
%{_libexecdir}/bluetooth/btvirt

%files cups
%_cups_serverbin/backend/bluetooth
%files hid2hci
/usr/lib/udev/hid2hci
%{_udevrulesdir}/97-hid2hci.rules

%files mesh
%config(noreplace) %{_sysconfdir}/bluetooth/mesh-main.conf
%{_bindir}/mesh-cfgclient
%{_bindir}/mesh-cfgtest
%{_datadir}/dbus-1/system.d/bluetooth-mesh.conf
%{_datadir}/dbus-1/system-services/org.bluez.mesh.service
%{_libexecdir}/bluetooth/bluetooth-meshd
%{_unitdir}/bluetooth-mesh.service
%{_localstatedir}/lib/bluetooth/mesh

%files obexd
%{_libexecdir}/bluetooth/obexd
%{_datadir}/dbus-1/services/org.bluez.obex.service
/usr/lib/systemd/user/dbus-org.bluez.obex.service
%{_datadir}/dbus-1/system.d/obex.conf
%{_userunitdir}/obex.service

%changelog
%autochangelog
