# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           appstream
Version:        1.2.1
Release:        %autorelease
Summary:        Utilities to generate, maintain and access the AppStream database
License:        LGPL-2.1-or-later
URL:            https://github.com/ximion/appstream
#!RemoteAsset:  sha256:2bc53d1d63ae28e7409a15747d4ae23a557409249461aab87a7947640402d1bd
Source:         https://github.com/ximion/appstream/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Ddocs=false
BuildOption(conf):  -Dapidocs=false
BuildOption(conf):  -Dman=false
BuildOption(conf):  -Dinstall-docs=false
BuildOption(conf):  -Dqt=true
BuildOption(conf):  -Dcompose=false
BuildOption(conf):  -Dstemming=false

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libfyaml)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(xmlb)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  itstool
BuildRequires:  gperf

%description
AppStream is a cross-distro effort for providing metadata for software
components in the Linux ecosystem.

%package        devel
Summary:        Development files for libappstream
Requires:       appstream%{?_isa} = %{version}-%{release}

%description    devel
Development files for AppStream.

%package        qt-devel
Summary:        Development files for %{name}-qt bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Core) >= 6.2.4

%description    qt-devel
%{summary}.

%install -a
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%doc README.md NEWS
%license COPYING
%{bash_completions_dir}/appstreamcli
%{_bindir}/appstreamcli
%{_datadir}/appstream/appstream.conf
%{_datadir}/gettext/its/metainfo.*
%{_datadir}/metainfo/org.freedesktop.appstream.cli.metainfo.xml
%exclude %{_datadir}/installed-tests/
%{_libdir}/libappstream.so.*
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/libAppStreamQt.so.*

%files devel
%{_includedir}/appstream/
%{_libdir}/libappstream.so
%{_libdir}/pkgconfig/appstream.pc
%{_datadir}/gir-1.0/*.gir

%files qt-devel
%{_includedir}/AppStreamQt/
%{_libdir}/cmake/AppStreamQt/
%{_libdir}/libAppStreamQt.so

%changelog
%autochangelog
