# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global __provides_exclude_from ^%{_libdir}/fcitx5/.*\\.so$

Name:           fcitx5-chinese-addons
Version:        5.1.12
Release:        %autorelease
Summary:        Chinese related addon for fcitx5
License:        LGPL-2.1-or-later
URL:            https://github.com/fcitx/fcitx5-chinese-addons
#!RemoteAsset:  sha256:99899bb014d8ffa778657939fb2cf219787cc56eac7cb2f98e5076764d467326
Source0:        https://download.fcitx-im.org/fcitx5/fcitx5-chinese-addons/fcitx5-chinese-addons-%{version}_dict.tar.zst
BuildSystem:    cmake

BuildOption(conf):  -DENABLE_BROWSER=OFF

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  ninja
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  cmake(Fcitx5Module)
BuildRequires:  cmake(Fcitx5ModuleLuaAddonLoader)
BuildRequires:  cmake(Fcitx5Qt6WidgetsAddons)
BuildRequires:  cmake(LibIMEPinyin)
BuildRequires:  cmake(LibIMETable)
BuildRequires:  cmake(OpenCC)
BuildRequires:  cmake(Qt6)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(libcurl)

Requires:       fcitx5
Requires:       fcitx5-lua

%description
This provides pinyin and table input method support for fcitx5.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%install -a
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%{_bindir}/scel2org5
%{_libdir}/fcitx5/*.so
%{_libdir}/fcitx5/qt6/*.so
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.ChineseAddons.metainfo.xml
%{_datadir}/fcitx5/addon/*.conf
%{_datadir}/fcitx5/inputmethod/*.conf
%{_datadir}/fcitx5/lua/imeapi/extensions/pinyin.lua
%dir %{_datadir}/fcitx5/pinyin
%{_datadir}/fcitx5/pinyin/*
%dir %{_datadir}/fcitx5/pinyinhelper
%{_datadir}/fcitx5/pinyinhelper/*
%dir %{_datadir}/fcitx5/punctuation
%{_datadir}/fcitx5/punctuation/*
%dir %{_datadir}/fcitx5/chttrans
%{_datadir}/fcitx5/chttrans/*

%files devel
%{_includedir}/Fcitx5/Module/fcitx-module/*
%{_libdir}/cmake/Fcitx5Module*

%changelog
%autochangelog
