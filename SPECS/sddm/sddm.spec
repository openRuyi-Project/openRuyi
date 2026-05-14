# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sddm
Version:        0.21.0
Release:        %autorelease
Summary:        QML-based display manager (Qt6)
License:        GPL-2.0-or-later
URL:            https://github.com/sddm/sddm
#!RemoteAsset:  sha256:f895de2683627e969e4849dbfbbb2b500787481ca5ba0de6d6dfdae5f1549abf
Source0:        https://github.com/sddm/sddm/archive/refs/tags/v%{version}.tar.gz
Source1:        sddm.conf
Source2:        sddm-greeter.pam
Source3:        sddm.pam
Source4:        sddm-autologin.pam
Source5:        sddm.sysusers
BuildSystem:    cmake

Patch0:         0001-CMake-Raise-required-version-to-3.5.patch
# https://github.com/sddm/sddm/pull/1779
Patch1:         0002-Redesign-login-shell-use-in-session-scripts.patch
# Part of https://github.com/sddm/sddm/pull/1896
Patch2:         0003-Fix-terminal-clearing.patch
# https://github.com/sddm/sddm/pull/1904
Patch3:         0004-Use-xrdb-to-set-Xcursor.theme.patch
# https://github.com/sddm/sddm/pull/1969
Patch4:         0005-Remove-unused-Display-m_relogin-variable.patch
Patch5:         0006-Set-Display-m_started-early.patch
Patch6:         0007-Load-autologin-configuration-in-Display-Display.patch
Patch7:         0008-Reset-daemonApp-first-in-the-Display-constructor.patch
Patch8:         0009-If-autologin-is-used-avoid-starting-a-display-server.patch

BuildOption(conf):  -DBUILD_WITH_QT6:BOOL=ON
BuildOption(conf):  -DBUILD_MAN_PAGES:BOOL=ON
BuildOption(conf):  -DENABLE_JOURNALD:BOOL=ON
# openruyi only wayland session
#BuildOption(conf):  -DSESSION_COMMAND:PATH=%{_sysconfdir}/X11/xinit/Xsession
BuildOption(conf):  -DWAYLAND_SESSION_COMMAND:PATH=%{_sysconfdir}/sddm/wayland-session

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig
BuildRequires:  shadow
BuildRequires:  python3dist(docutils)
BuildRequires:  qt6-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  qt6-linguist
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xcb-xkb)

Requires:       mesa-gl
Requires:       fonts-dejavu
Requires:       fonts-unifont
Requires:       weston
Requires:       xcursor-themes

%{?systemd_requires}

%description
SDDM is a modern graphical display manager aiming to be fast, simple and
beautiful. It uses modern technologies like QtQuick, which in turn gives the
designer the ability to create smooth, animated user interfaces.

%install -a
mkdir -p %{buildroot}%{_sysconfdir}/sddm.conf.d
mkdir -p %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d
install -Dpm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pam.d/sddm
install -Dpm 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/pam.d/sddm-autologin
install -Dpm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pam.d/sddm-greeter
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sddm.conf
install -Dpm 644 %{SOURCE5} %{buildroot}%{_sysusersdir}/sddm.conf
mkdir -p %{buildroot}/run/sddm
mkdir -p %{buildroot}%{_localstatedir}/lib/sddm
mkdir -p %{buildroot}%{_sysconfdir}/sddm/
cp -a %{buildroot}%{_datadir}/sddm/scripts/* \
      %{buildroot}%{_sysconfdir}/sddm/
rm -fv %{buildroot}%{_sysconfdir}/sddm/Xsession

# De-conflict the dbus file
mv %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager.conf \
   %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-sddm.conf

%pre
%sysusers_create_package %{name} %{SOURCE5}

%post
%systemd_post sddm.service

%preun
%systemd_preun sddm.service

%postun
%systemd_postun sddm.service

%files
%license LICENSE
%doc README.md CONTRIBUTORS
%dir %{_sysconfdir}/sddm/
%dir %{_sysconfdir}/sddm.conf.d
%dir %{_prefix}/lib/sddm/sddm.conf.d
%config(noreplace) %{_sysconfdir}/sddm/*
%config(noreplace) %{_sysconfdir}/sddm.conf
%config(noreplace) %{_sysconfdir}/pam.d/sddm*
%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-sddm.conf
%{_bindir}/sddm
%{_bindir}/sddm-greeter*
%{_libexecdir}/sddm-helper
%{_libexecdir}/sddm-helper-start-wayland
%{_libexecdir}/sddm-helper-start-x11user
%{_tmpfilesdir}/sddm.conf
%{_sysusersdir}/sddm.conf
%attr(0711, root, sddm) %dir /run/sddm
%attr(1770, sddm, sddm) %dir %{_localstatedir}/lib/sddm
%{_unitdir}/sddm.service
%{_qt6_archdatadir}/qml/SddmComponents/
%dir %{_datadir}/sddm
%{_datadir}/sddm/faces/
%{_datadir}/sddm/flags/
%{_datadir}/sddm/scripts/
%dir %{_datadir}/sddm/themes/
%{_datadir}/sddm/translations*/
%{_mandir}/man1/sddm.1*
%{_mandir}/man1/sddm-greeter.1*
%{_mandir}/man5/sddm.conf.5*
%{_mandir}/man5/sddm-state.conf.5*
%{_datadir}/sddm/themes/elarun/
%{_datadir}/sddm/themes/maldives/
%{_datadir}/sddm/themes/maya/

%changelog
%autochangelog
