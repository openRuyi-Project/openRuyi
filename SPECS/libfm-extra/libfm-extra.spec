# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libfm-extra
Version:        1.3.2
Release:        %autorelease
Summary:        Extra library from the LibFM file manager framework
License:        LGPL-2.1-or-later
URL:            https://sourceforge.net/projects/pcmanfm/
VCS:            git:https://github.com/lxde/libfm.git
#!RemoteAsset:  sha256:a5042630304cf8e5d8cff9d565c6bd546f228b48c960153ed366a34e87cad1e5
Source0:        https://downloads.sourceforge.net/project/pcmanfm/PCManFM%20%2B%20Libfm%20%28tarball%20release%29/LibFM/libfm-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(prep):  -n libfm-%{version}
BuildOption(conf):  --with-extra-only
BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-gtk-doc

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.22.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)

%description
libfm-extra is the standalone extra library from LibFM. It provides XML helper
APIs used by LibFM-based file manager components without building the full
LibFM stack.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%conf -p
autoreconf -fiv

%files
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/libfm-extra.so.*

%files devel
%{_includedir}/libfm
%{_includedir}/libfm-1.0/
%{_libdir}/libfm-extra.so
%{_libdir}/pkgconfig/libfm-extra.pc

%changelog
%autochangelog
