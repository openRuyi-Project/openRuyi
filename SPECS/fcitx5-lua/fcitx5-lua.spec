# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:           fcitx5-lua
Version:        5.0.16
Release:        %autorelease
Summary:        Lua support for fcitx5
License:        LGPL-2.1-or-later
URL:            https://github.com/fcitx/fcitx5-lua
#!RemoteAsset:  sha256:424e0f1a3766247e0cc561d52749cc832ba885f47026b0a58c10610c9bf251fe
Source0:        https://download.fcitx-im.org/fcitx5/fcitx5-lua/fcitx5-lua-%{version}.tar.zst
BuildSystem:    cmake

BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  ninja
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  cmake(Fcitx5Module)
BuildRequires:  pkgconfig(lua)

Requires:       fcitx5

%description
Lua support for fcitx5.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fcitx5-devel

%description    devel
Development files for %{name}.

%install -a
%find_lang %{name} --generate-subpackages

# testlua segfaults without keyboard-us IM engine in build env
%check

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%{_libdir}/fcitx5/libluaaddonloader.so
%{_datadir}/fcitx5/addon/imeapi.conf
%{_datadir}/fcitx5/addon/luaaddonloader.conf
%{_datadir}/fcitx5/lua
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Lua.metainfo.xml

%files devel
%{_includedir}/Fcitx5/Module/fcitx-module/luaaddonloader
%{_libdir}/cmake/Fcitx5ModuleLuaAddonLoader

%changelog
%autochangelog
