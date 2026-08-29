# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Prefer %%global; allow external override for _kf6_prefix

%{lua:
if posix.stat(rpm.expand('%{SOURCE0}')) then
  rpm.load(rpm.expand('%{SOURCE0}'))
end
}

Name:           kf6-rpm-macros
Version:        20251125
Release:        %autorelease
Summary:        RPM macros for KDE packages using Qt6
License:        MIT
Source0:        macros.kf6
BuildArch:      noarch

Requires:       cmake
Requires:       hicolor-icon-theme
Requires:       ninja

%description
This package contains macros which are used when building KDE packages.

%prep

%build

%install
install -D -m0644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf6

mkdir -p %{buildroot}%{_kf6_includedir}
mkdir -p %{buildroot}%{_kf6_libexecdir}
mkdir -p %{buildroot}%{_kf6_datadir}
mkdir -p %{buildroot}%{_kf6_configkcfgdir}
mkdir -p %{buildroot}%{_kf6_htmldir}
mkdir -p %{buildroot}%{_kf6_notificationsdir}
mkdir -p %{buildroot}%{_kf6_knsrcfilesdir}
mkdir -p %{buildroot}%{_kf6_kxmlguidir}
mkdir -p %{buildroot}%{_kf6_localedir}
mkdir -p %{buildroot}%{_kf6_plasmadir}
mkdir -p %{buildroot}%{_kf6_debugdir}
mkdir -p %{buildroot}%{_kf6_wallpapersdir}
mkdir -p %{buildroot}%{_includedir}/KPim6
mkdir -p %{buildroot}%{_kf6_libdir}/kconf_update_bin
mkdir -p %{buildroot}%{_kf6_libexecdir}/kauth
mkdir -p %{buildroot}%{_kf6_plugindir}/designer
mkdir -p %{buildroot}%{_kf6_plugindir}/kf6
mkdir -p %{buildroot}%{_kf6_plugindir}/kf6/kded
mkdir -p %{buildroot}%{_kf6_plugindir}/kf6/kio
mkdir -p %{buildroot}%{_kf6_plugindir}/kf6/parts
mkdir -p %{buildroot}%{_kf6_plugindir}/pim6
mkdir -p %{buildroot}%{_kf6_plugindir}/pim6/akonadi
mkdir -p %{buildroot}%{_kf6_plugindir}/plasma/applets
mkdir -p %{buildroot}%{_kf6_plugindir}/plasma/kcms/systemsettings
mkdir -p %{buildroot}%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets
mkdir -p %{buildroot}%{_kf6_qmldir}/org/kde
mkdir -p %{buildroot}%{_kf6_sharedir}/kconf_update
mkdir -p %{buildroot}%{_kf6_sharedir}/kdevappwizard/templates
mkdir -p %{buildroot}%{_kf6_sharedir}/kglobalaccel
mkdir -p %{buildroot}%{_kf6_sharedir}/krunner/dbusplugins
mkdir -p %{buildroot}%{_kf6_sharedir}/plasma/plasmoids

%files
%{_rpmconfigdir}/macros.d/macros.kf6
%dir %{_kf6_configkcfgdir}
%dir %{_kf6_datadir}
%dir %{_kf6_debugdir}
%dir %{_kf6_htmldir}
%dir %{_kf6_includedir}
%dir %{_kf6_knsrcfilesdir}
%dir %{_kf6_kxmlguidir}
%dir %{_kf6_libexecdir}
%dir %{_kf6_localedir}
%dir %{_kf6_notificationsdir}
%dir %{_kf6_plasmadir}
%dir %{_kf6_wallpapersdir}
%dir %{_includedir}/KPim6
%dir %{_kf6_libdir}/kconf_update_bin
%dir %{_kf6_libdir}/qt6
%dir %{_kf6_libexecdir}/kauth
%dir %{_kf6_plugindir}
%dir %{_kf6_plugindir}/designer
%dir %{_kf6_plugindir}/kf6
%dir %{_kf6_plugindir}/kf6/kded
%dir %{_kf6_plugindir}/kf6/kio
%dir %{_kf6_plugindir}/kf6/parts
%dir %{_kf6_plugindir}/pim6
%dir %{_kf6_plugindir}/pim6/akonadi
%dir %{_kf6_plugindir}/plasma
%dir %{_kf6_plugindir}/plasma/applets
%dir %{_kf6_plugindir}/plasma/kcms
%dir %{_kf6_plugindir}/plasma/kcms/systemsettings
%dir %{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets
%dir %{_kf6_qmldir}
%dir %{_kf6_qmldir}/org
%dir %{_kf6_qmldir}/org/kde
%dir %{_kf6_sharedir}/kconf_update
%dir %{_kf6_sharedir}/kdevappwizard
%dir %{_kf6_sharedir}/kdevappwizard/templates
%dir %{_kf6_sharedir}/kglobalaccel
%dir %{_kf6_sharedir}/krunner
%dir %{_kf6_sharedir}/krunner/dbusplugins

%changelog
%autochangelog
