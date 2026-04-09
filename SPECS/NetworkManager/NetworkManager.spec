# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond modem_manager 0

# Got lazy
%global _pppddir %(ls -d %{_libdir}/pppd/2.?.?)

Name:           NetworkManager
Version:        1.54.3
Release:        %autorelease
Summary:        Standard Linux network configuration tool suite
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://networkmanager.dev/
VCS:            git:https://gitlab.freedesktop.org/NetworkManager/NetworkManager
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/archive/%{version}/downloads/%{name}-%{version}.tar.gz
Source1:        NetworkManager.conf
Source2:        connectivity.conf
BuildSystem:    meson

BuildOption(conf):  -Dmodem_manager=%{?with_modem_manager:true}%{!?with_modem_manager:false}
BuildOption(conf):  -Ddhclient=%{_sbindir}/dhclient
BuildOption(conf):  -Ddhcpcd=no
BuildOption(conf):  -Dcrypto=gnutls
BuildOption(conf):  -Dmore_logging=false
BuildOption(conf):  -Dmore_asserts=0
BuildOption(conf):  -Db_lto=true
BuildOption(conf):  -Dlibaudit=yes-disabled-by-default
BuildOption(conf):  -Dwifi=true
BuildOption(conf):  -Diwd=true
BuildOption(conf):  -Dbluez5_dun=true
BuildOption(conf):  -Dnm_cloud_setup=true
BuildOption(conf):  -Ddocs=true
BuildOption(conf):  -Dqt=false
BuildOption(conf):  -Dovs=true
BuildOption(conf):  -Dppp=true
BuildOption(conf):  -Dpppd=%{_sbindir}/pppd
BuildOption(conf):  -Dpppd_plugin_dir=%{_pppddir}
BuildOption(conf):  -Dsession_tracking=systemd
BuildOption(conf):  -Dsystemdsystemunitdir=%{_unitdir}
BuildOption(conf):  -Ddbus_conf_dir=%{_datadir}/dbus-1/system.d
BuildOption(conf):  -Ddist_version=%{version}-%{release}
BuildOption(conf):  -Dnetconfig=no
# TODO: not every linux distro enabled this, can be changed later
BuildOption(conf):  -Dtests=no

BuildRequires:  meson
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libndp)
BuildRequires:  pkgconfig(libnewt)
BuildRequires:  pkgconfig(libnvme)
BuildRequires:  pkgconfig(libpsl)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxslt)

%if %{with modem_manager}
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(mobile-broadband-provider-info)
%endif

BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pppd)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  python3
BuildRequires:  python3-dbus
BuildRequires:  python3-pygobject
BuildRequires:  vala

%description
NetworkManager is a system service that manages network interfaces and
connections using either user-defined settings or automatic configuration.
It supports Ethernet as well as Bridge, Bond, VLAN, Team, InfiniBand, Wi-Fi,
mobile broadband (WWAN), PPPoE, and other device types, and it works with
a wide range of VPN services.

%package        plugins
Summary:        Plugins for NetworkManager
Requires:       %{name}%{?_isa} = %{version}-%{release}
# PPPoE (adsl)
Requires:       ppp
# Bluetooth
Requires:       bluez
# wwan (Mobile broadband)
Requires:       ModemManager
# ovs (Open vSwitch)
Requires:       openvswitch
# Wi-Fi
Requires:       wpa_supplicant

%description    plugins
This package contains various plugins for NetworkManager, for example
pppoe, bluetooth, ovs, wifi, etc.

%package        tui
Summary:        NetworkManager curses-based UI
Requires:       %{name} = %{version}-%{release}
Requires:       libnm%{?_isa} = %{version}-%{release}

%description    tui
This adds a curses-based "TUI" (Text User Interface) to
NetworkManager, to allow performing some of the operations supported
by nm-connection-editor and nm-applet in a non-graphical environment.

%package        cloud-setup
Summary:        Automatically configure NetworkManager in cloud
Requires:       %{name} = %{version}
Requires:       libnm%{?_isa} = %{version}-%{release}

%description    cloud-setup
Installs a nm-cloud-setup tool that can automatically configure
NetworkManager in cloud environment. Only certain cloud providers
like Aliyun, Azure, EC2, GCP are supported.

%package     -n libnm
Summary:        Libraries for adding NetworkManager support to applications.
License:        LGPL-2.1-or-later

%description -n libnm
This package contains the libraries that make it easier to use some
NetworkManager functionality from applications.

%package     -n libnm-devel
Summary:        Header files for adding NetworkManager support to applications.
License:        LGPL-2.1-or-later
Requires:       libnm%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       pkgconfig(glib-2.0)

%description -n libnm-devel
This package contains the header and pkg-config files for development
applications using NetworkManager functionality from applications.

%install -a
install -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/NetworkManager/
install -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/NetworkManager/conf.d
# TODO: Avoid illegal locale package name
rm -rf %{buildroot}%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

# TODO: We purposely disable tests for now
%check

%post
%systemd_post NetworkManager.service NetworkManager-wait-online.service NetworkManager-dispatcher.service nm-priv-helper.service

%post cloud-setup
%systemd_post nm-cloud-setup.service

%preun
%systemd_preun NetworkManager.service NetworkManager-wait-online.service NetworkManager-dispatcher.service nm-priv-helper.service

%preun cloud-setup
%systemd_preun nm-cloud-setup.service

%postun
%systemd_postun NetworkManager.service NetworkManager-wait-online.service NetworkManager-dispatcher.service nm-priv-helper.service

%postun cloud-setup
%systemd_postun nm-cloud-setup.service

%files -f %{name}.lang
%doc ChangeLog NEWS AUTHORS TODO
%license COPYING
%{_bindir}/nm-online
%{_bindir}/nmcli
%{_datadir}/bash-completion/completions/nmcli
%{_sbindir}/NetworkManager
%{_datadir}/dbus-1/system-services/org.freedesktop.nm_dispatcher.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.NetworkManager.*
%{_datadir}/polkit-1/actions/org.freedesktop.NetworkManager.policy
%attr(0700,root,root) %{_localstatedir}/lib/NetworkManager
%{_mandir}/man1/nm-online.1*
%{_mandir}/man1/nmcli.1*
%{_mandir}/man5/nm-settings-keyfile.5*
%{_mandir}/man5/NetworkManager.conf.5*
%{_mandir}/man5/nm-settings.5*
%{_mandir}/man5/nm-system-settings.conf.5*
%{_mandir}/man5/nm-settings-dbus.5*
%{_mandir}/man5/nm-settings-nmcli.5*
%{_mandir}/man7/nmcli-examples.7*
%{_mandir}/man8/NetworkManager-dispatcher.8*
%{_mandir}/man8/NetworkManager-wait-online.service.8*
%{_mandir}/man8/NetworkManager.8*
%{_mandir}/man8/nm-initrd-generator.8*
%dir %{_libdir}/NetworkManager
%{_libexecdir}/nm-daemon-helper
%{_libexecdir}/nm-libnm-helper
%{_libexecdir}/nm-dhcp-helper
%{_libexecdir}/nm-dispatcher
%{_libexecdir}/nm-initrd-generator
%{_libexecdir}/nm-priv-helper
%dir %{_sysconfdir}/NetworkManager
%dir %{_sysconfdir}/NetworkManager/conf.d
%dir %{_sysconfdir}/NetworkManager/dispatcher.d
%dir %{_sysconfdir}/NetworkManager/system-connections
%{_unitdir}/NetworkManager.service
%{_unitdir}/NetworkManager-dispatcher.service
%{_unitdir}/NetworkManager-wait-online.service
%dir %{_unitdir}/NetworkManager.service.d
%{_prefix}/lib/udev/rules.d/84-nm-drivers.rules
%{_prefix}/lib/udev/rules.d/85-nm-unmanaged.rules
%{_prefix}/lib/udev/rules.d/90-nm-thunderbolt.rules
%{_unitdir}/nm-priv-helper.service
%dir %{_datadir}/doc/NetworkManager/examples
%{_datadir}/doc/NetworkManager/examples/server.conf
%ghost %config(noreplace) %{_localstatedir}/log/NetworkManager
%dir %{_prefix}/lib/NetworkManager
%{_prefix}/lib/NetworkManager/NetworkManager.conf
%dir %{_prefix}/lib/NetworkManager/conf.d
%dir %{_prefix}/lib/NetworkManager/dispatcher.d
%dir %{_prefix}/lib/NetworkManager/dispatcher.d/no-wait.d
%dir %{_prefix}/lib/NetworkManager/dispatcher.d/pre-up.d
%dir %{_prefix}/lib/NetworkManager/dispatcher.d/pre-down.d
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/zones
%{_prefix}/lib/firewalld/zones/nm-shared.xml
%{_datadir}/dbus-1/system.d/nm-dispatcher.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.NetworkManager.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.nm_priv_helper.service
%{_datadir}/dbus-1/system.d/nm-priv-helper.conf
%{_unitdir}/NetworkManager-config-initrd.service
%{_unitdir}/NetworkManager-initrd.service
%{_unitdir}/NetworkManager-wait-online-initrd.service
# Connectivity files
%{_prefix}/lib/NetworkManager/conf.d/connectivity.conf

%files plugins
%dir %{_libdir}/NetworkManager/%{version}-%{release}
# PPPoE (adsl)
%{_libdir}/NetworkManager/%{version}-%{release}/libnm-device-plugin-adsl.so
%{_libdir}/NetworkManager/%{version}-%{release}/libnm-ppp-plugin.so
%dir %{_libdir}/pppd/2.*
%{_libdir}/pppd/2.*/nm-pppd-plugin.*

%if %{with modem_manager}
# Bluetooth
%{_libdir}/NetworkManager/%{version}-%{release}/libnm-device-plugin-bluetooth.so
# wwan (Mobile broadband)
%{_libdir}/NetworkManager/%{version}-%{release}/libnm-device-plugin-wwan.so
%{_libdir}/NetworkManager/%{version}-%{release}/libnm-wwan.so
%endif

# ovs (Open vSwitch)
%{_libdir}/NetworkManager/%{version}-%{release}/libnm-device-plugin-ovs.so
%{_unitdir}/NetworkManager.service.d/NetworkManager-ovs.conf
%{_mandir}/man7/nm-openvswitch.7*
# Wi-Fi
%{_libdir}/NetworkManager/%{version}-%{release}/libnm-device-plugin-wifi.so
%files tui
%{_bindir}/nmtui*
%{_mandir}/man1/nmtui.1*
%{_mandir}/man1/nmtui-connect.1*
%{_mandir}/man1/nmtui-edit.1*
%{_mandir}/man1/nmtui-hostname.1*

%files cloud-setup
%{_libexecdir}/nm-cloud-setup
%{_unitdir}/nm-cloud-setup.service
%{_unitdir}/nm-cloud-setup.timer
%{_prefix}/lib/NetworkManager/dispatcher.d/90-nm-cloud-setup.sh
%{_prefix}/lib/NetworkManager/dispatcher.d/no-wait.d/90-nm-cloud-setup.sh
%{_prefix}/lib/NetworkManager/dispatcher.d/pre-up.d/90-nm-cloud-setup.sh
%{_mandir}/man8/nm-cloud-setup.8*

%files -n libnm
%{_libdir}/libnm.so.*
%{_libdir}/girepository-1.0/NM-1.0.typelib

%files -n libnm-devel
%{_includedir}/libnm/
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libnm.deps
%{_datadir}/vala/vapi/libnm.vapi
%{_libdir}/libnm.so
%{_libdir}/pkgconfig/libnm.pc
%doc %{_datadir}/gtk-doc/html/NetworkManager/
%doc %{_datadir}/gtk-doc/html/libnm/

%changelog
%autochangelog
