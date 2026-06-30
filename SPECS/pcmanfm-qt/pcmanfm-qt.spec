# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pcmanfm-qt
Version:        2.4.0
Release:        %autorelease
Summary:        Qt file manager and desktop handler for LXQt
License:        GPL-2.0-or-later
URL:            https://github.com/lxqt/pcmanfm-qt
VCS:            git:https://github.com/lxqt/pcmanfm-qt.git
#!RemoteAsset:  sha256:53fb1acf5a818300487ceffabc5b768034fa4dee956b9d1bc0019bb456b48daf
Source0:        https://github.com/lxqt/pcmanfm-qt/releases/download/%{version}/pcmanfm-qt-%{version}.tar.xz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(LayerShellQt) >= 6.0.0
BuildRequires:  cmake(Qt6DBus) >= 6.6.0
BuildRequires:  cmake(Qt6LinguistTools) >= 6.6.0
BuildRequires:  cmake(Qt6Widgets) >= 6.6.0
BuildRequires:  cmake(fm-qt6) >= 2.4.0
BuildRequires:  cmake(lxqt2-build-tools) >= 2.4.0

Requires:       layer-shell-qt >= 6.0.0
Requires:       libfm-qt >= 2.4.0

%description
PCManFM-Qt is a Qt-based file manager and desktop handler. It is the Qt port
of PCManFM and can be used by LXQt or independently in other desktop
environments.

%install -a
%find_lang %{name} --generate-subpackages --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-desktop-pref.desktop
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/lxqt-desktop.desktop

%files -f %{name}.lang
%doc AUTHORS CHANGELOG README.md
%license LICENSE
%{_bindir}/pcmanfm-qt
%{_datadir}/applications/pcmanfm-qt.desktop
%{_datadir}/applications/pcmanfm-qt-desktop-pref.desktop
%{_datadir}/icons/hicolor/scalable/apps/pcmanfm-qt.svg
%dir %{_datadir}/pcmanfm-qt
%dir %{_datadir}/pcmanfm-qt/lxqt
%{_datadir}/pcmanfm-qt/lxqt/settings.conf
%dir %{_datadir}/pcmanfm-qt/translations
%{_mandir}/man1/pcmanfm-qt.1*
%config(noreplace) %{_sysconfdir}/xdg/autostart/lxqt-desktop.desktop

%changelog
%autochangelog
