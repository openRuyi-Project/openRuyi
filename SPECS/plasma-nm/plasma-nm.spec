# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.18.0
%define qt6_version 6.9.0

%bcond vpn 0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}

Name:           plasma-nm
Version:        6.7.1
Release:        %autorelease
Summary:        Plasma applet written in QML for managing network connections
License:        (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/plasma/plasma-nm.git
#!RemoteAsset:  sha256:9d368d63f60d7743e900e0aebaf1de800226961d403a25c0362bfeb9c4ffa107
Source:         https://invent.kde.org/plasma/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF
BuildOption(conf):  -DQT_QML_NO_CACHEGEN:BOOL=TRUE

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  kirigami-addons
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Declarative) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6ModemManagerQt) >= %{kf6_version}
BuildRequires:  cmake(KF6NetworkManagerQt) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Prison) >= %{kf6_version}
BuildRequires:  cmake(KF6QuickCharts) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(QCoro6DBus)
BuildRequires:  cmake(Qca-qt6) >= 2.1.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(libnm) >= 1.4.0
BuildRequires:  pkgconfig(mobile-broadband-provider-info)
BuildRequires:  pkgconfig(openconnect) >= 5.2
BuildRequires:  pkgconfig(openssl)

Requires:       NetworkManager
Requires:       kf6-kded
Requires:       kf6-kirigami >= %{kf6_version}
Requires:       kf6-networkmanager-qt >= %{kf6_version}
Requires:       kf6-prison >= %{kf6_version}
Requires:       kwalletd6
Requires:       systemsettings

Recommends:     mobile-broadband-provider-info

Provides:       NetworkManager-client

%description
Plasma applet for controlling network connections on systems
that use the NetworkManager service.

%if %{with vpn}
%package        openvpn
Summary:        OpenVPN support for plasma-nm
Requires:       NetworkManager-openvpn
Requires:       %{name}%{?_isa} = %{version}-%{release}
Supplements:    (plasma-nm and NetworkManager-openvpn)
Provides:       NetworkManager-openvpn-frontend
Provides:       plasma-nm-openvpn = %{version}
Obsoletes:      plasma-nm-openvpn < %{version}

%description    openvpn
OpenVPN plugin for plasma-nm components.

%package        vpnc
Summary:        vpnc support for plasma-nm
Requires:       NetworkManager-vpnc
Requires:       %{name}%{?_isa} = %{version}-%{release}
Supplements:    (plasma-nm and NetworkManager-vpnc)
Provides:       NetworkManager-vpnc-frontend
Provides:       plasma-nm-vpnc = %{version}
Obsoletes:      plasma-nm-vpnc < %{version}

%description    vpnc
vpnc plugin for plasma-nm components.

%package        openconnect
Summary:        OpenConnect support for plasma-nm
Requires:       NetworkManager-openconnect
Requires:       openconnect
Requires:       %{name}%{?_isa} = %{version}-%{release}
Supplements:    (plasma-nm and NetworkManager-openconnect)
Provides:       NetworkManager-openconnect-frontend
Provides:       plasma-nm-openconnect = %{version}
Obsoletes:      plasma-nm-openconnect < %{version}

%description    openconnect
OpenConnect plugin for plasma-nm components.

%package        libreswan
Summary:        Libreswan support for plasma-nm
Requires:       NetworkManager-libreswan
Requires:       %{name}%{?_isa} = %{version}-%{release}
Supplements:    (plasma-nm and NetworkManager-libreswan)
Provides:       NetworkManager-libreswan-frontend
Provides:       plasma-nm-openswan = %{version}
Obsoletes:      plasma-nm-openswan < %{version}

%description    libreswan
Libreswan plugin for plasma-nm components.

%package        strongswan
Summary:        strongSwan support for plasma-nm
Requires:       NetworkManager-strongswan
Requires:       %{name}%{?_isa} = %{version}-%{release}
Supplements:    (plasma-nm and NetworkManager-strongswan)
Provides:       NetworkManager-strongswan-frontend
Provides:       plasma-nm-strongswan = %{version}
Obsoletes:      plasma-nm-strongswan < %{version}

%description    strongswan
strongSwan plugin for plasma-nm components.

%package        l2tp
Summary:        L2TP support for plasma-nm
Requires:       NetworkManager-l2tp
Requires:       %{name}%{?_isa} = %{version}-%{release}
Supplements:    (plasma-nm and NetworkManager-l2tp)
Provides:       NetworkManager-l2tp-frontend
Provides:       plasma-nm-l2tp = %{version}
Obsoletes:      plasma-nm-l2tp < %{version}

%description    l2tp
Layer Two Tunneling Protocol (L2TP) plugin for plasma-nm components.

%package        pptp
Summary:        PPTP support for plasma-nm
Requires:       NetworkManager-pptp
Requires:       %{name}%{?_isa} = %{version}-%{release}
Supplements:    (plasma-nm and NetworkManager-pptp)
Provides:       NetworkManager-pptp-frontend
Provides:       plasma-nm-pptp = %{version}
Obsoletes:      plasma-nm-pptp < %{version}

%description    pptp
Point-To-Point Tunneling Protocol (PPTP) plugin for plasma-nm components.

%package        ssh
Summary:        SSH support for plasma-nm
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-ssh
Supplements:    (plasma-nm and NetworkManager-ssh)
Provides:       NetworkManager-ssh-frontend

%description    ssh
Secure Shell (SSH) plugin for plasma-nm components.

%package        sstp
Summary:        SSTP support for plasma-nm
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-sstp
Supplements:    (plasma-nm and NetworkManager-sstp)
Provides:       NetworkManager-sstp-frontend

%description    sstp
Secure Sockets Tunneling Protocol (SSTP) plugin for plasma-nm components.

%package        iodine
Summary:        VPN support for plasma-nm
Requires:       NetworkManager-iodine
Requires:       %{name}%{?_isa} = %{version}-%{release}
Supplements:    (plasma-nm and NetworkManager-iodine)
Provides:       NetworkManager-iodine-frontend

%description    iodine
Iodine (VPN through DNS tunnel) plugin for plasma-nm components.

%package        fortisslvpn
Summary:        FortiGate SSL VPN support for plasma-nm
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-fortisslvpn
Supplements:    (plasma-nm and NetworkManager-fortisslvpn)
Provides:       NetworkManager-fortisslvpn-frontend

%description    fortisslvpn
FortiGate SSL VPN plugin for plasma-nm components.
%endif

%install -a
# Disable VPN payload when vpn bcond is off
%if %{without vpn}
rm -rf %{buildroot}%{_kf6_plugindir}/plasma/network/vpn/*
%endif

# Use langpacks macro to auto-split translations
%find_lang %{name} --with-qt --all-name --generate-subpackages

%files -f %{name}.lang
%license LICENSES/*
%dir %{_kf6_plugindir}/plasma/network
%if %{with vpn}
%dir %{_kf6_plugindir}/plasma/network/vpn
%endif
%{_kf6_applicationsdir}/kcm_cellular_network.desktop
%{_kf6_applicationsdir}/kcm_mobile_hotspot.desktop
%{_kf6_applicationsdir}/kcm_mobile_wired.desktop
%{_kf6_applicationsdir}/kcm_mobile_wifi.desktop
%{_kf6_applicationsdir}/kcm_networkmanagement.desktop
%{_kf6_applicationsdir}/org.kde.vpnimport.desktop
%{_kf6_debugdir}/plasma-nm.categories
%{_kf6_libdir}/libplasmanm_cellular.so
%{_kf6_libdir}/libplasmanm_editor.so
%{_kf6_libdir}/libplasmanm_internal.so
%{_kf6_notificationsdir}/networkmanagement.notifyrc
%{_kf6_plugindir}/kf6/kded/networkmanagement.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_cellular_network.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_hotspot.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_wired.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_wifi.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_networkmanagement.so
%dir %{_kf6_plugindir}/plasma/applets/
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.networkmanagement.so
%dir %{_kf6_qmldir}/org/kde/plasma
%{_kf6_qmldir}/org/kde/plasma/networkmanagement/
%{_kf6_sharedir}/kcm_networkmanagement/

%if %{with vpn}
%files openvpn
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openvpnui.so

%files vpnc
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_vpncui.so

%files openconnect
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_anyconnect.so
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_arrayui.so
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_f5ui.so
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_fortinetui.so
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_globalprotectui.so
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_juniperui.so
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_pulseui.so

%files libreswan
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_libreswanui.so

%files strongswan
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_strongswanui.so

%files l2tp
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_l2tpui.so

%files pptp
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_pptpui.so

%files ssh
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_sshui.so

%files sstp
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_sstpui.so

%files iodine
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_iodineui.so

%files fortisslvpn
%{_kf6_plugindir}/plasma/network/vpn/plasmanetworkmanagement_fortisslvpnui.so
%endif

%changelog
%autochangelog
