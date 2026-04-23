# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           adwaita-icon-theme
Version:        50.0
Release:        %autorelease
Summary:        Adwaita icon theme
License:        LGPL-3.0-only OR CC-BY-SA-3.0
URL:            https://gitlab.gnome.org/GNOME/adwaita-icon-theme
#!RemoteAsset:  sha256:fac6e0401fca714780561a081b8f7e27c3bc1db34ebda4da175081f26b24d460
Source0:        https://download.gnome.org/sources/adwaita-icon-theme/50/adwaita-icon-theme-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)

%description
This package contains the Adwaita icon theme used by the GNOME desktop.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains the pkgconfig file for
developing applications that use %{name}.

%install -a
touch %{buildroot}%{_datadir}/icons/Adwaita/.icon-theme.cache

%transfiletriggerin -- %{_datadir}/icons/Adwaita
if [ -x /usr/bin/gtk4-update-icon-cache ]; then
  /usr/bin/gtk4-update-icon-cache --force %{_datadir}/icons/Adwaita &>/dev/null || :
elif [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --force %{_datadir}/icons/Adwaita &>/dev/null || :
fi

%transfiletriggerpostun -- %{_datadir}/icons/Adwaita
if [ -x /usr/bin/gtk4-update-icon-cache ]; then
  /usr/bin/gtk4-update-icon-cache --force %{_datadir}/icons/Adwaita &>/dev/null || :
elif [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --force %{_datadir}/icons/Adwaita &>/dev/null || :
fi

%files
%license COPYING*
%{_datadir}/icons/Adwaita/16x16/
%{_datadir}/icons/Adwaita/scalable/
%{_datadir}/icons/Adwaita/symbolic/
%{_datadir}/icons/Adwaita/index.theme
%ghost %{_datadir}/icons/Adwaita/.icon-theme.cache
%dir %{_datadir}/icons/Adwaita/
%{_datadir}/icons/Adwaita/cursors/

%files devel
%{_datadir}/pkgconfig/adwaita-icon-theme.pc

%changelog
%autochangelog
