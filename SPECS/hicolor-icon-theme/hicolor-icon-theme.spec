# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define hicolor_dir_list {{actions,\
animations,apps,categories,devices,emblems,emotes,filesystems,\
intl,mimetypes,places,status,\
stock,stock/chart,stock/code,stock/data,stock/form,\
stock/image,stock/io,stock/media,stock/navigation,\
stock/net,stock/object,stock/table,stock/text}} %{nil}

Name:           hicolor-icon-theme
Version:        0.18
Release:        %autorelease
Summary:        Fallback Icon Theme
License:        GPL-2.0-or-later
URL:            https://freedesktop.org/wiki/Software/icon-theme/
VCS:            git:https://gitlab.freedesktop.org/xdg/default-icon-theme
#!RemoteAsset
Source:         https://icon-theme.freedesktop.org/releases/hicolor-icon-theme-%{version}.tar.xz
BuildArch:      noarch
BuildSystem:    meson

BuildRequires:  meson

%description
The default fallback theme for the FreeDesktop.org icon specification, providi
ng directory scaffolding, metadata, and pkg-config macros so applications can
rely on consistent icon lookup.

%install -a
touch %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache
chmod -x COPYING
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{1024x1024,1024x1024@2}/%{hicolor_dir_list}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/symbolic/%{hicolor_dir_list}

%files
%license COPYING
%doc NEWS README.md
%ghost %{_datadir}/icons/hicolor/icon-theme.cache
%{_datadir}/icons/hicolor/
%{_datadir}/pkgconfig/default-icon-theme.pc

%changelog
%autochangelog
