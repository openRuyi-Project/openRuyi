# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libxcb
Version:        1.17.0
Release:        %autorelease
Summary:        A C binding to the X11 protocol
License:        X11
URL:            https://xcb.freedesktop.org/
VCS:            git:https://gitlab.freedesktop.org/xorg/lib/libxcb.git
#!RemoteAsset:  sha256:599ebf9996710fea71622e6e184f3a8ad5b43d0e5fa8c4e407123c88a59a6d55
Source0:        https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
# This is stolen straight from the pthread-stubs source:
# http://cgit.freedesktop.org/xcb/pthread-stubs/blob/?id=6900598192bacf5fd9a34619b11328f746a5956d
# We need the pkgconfig file so
Source1:        pthread-stubs.pc.in
BuildSystem:    autotools

BuildOption(conf):  --enable-selinux
BuildOption(conf):  --enable-xkb
BuildOption(conf):  --enable-xinput
BuildOption(conf):  --disable-xprint
BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --enable-unit-tests
BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(xorg-macros) >= 1.18
BuildRequires:  pkgconfig(xau) >= 0.99.2
BuildRequires:  pkgconfig(xcb-proto) >= 1.17.0
BuildRequires:  doxygen
BuildRequires:  pkgconfig(python3)

%description
The X protocol C-language Binding (XCB) is a replacement for Xlib featuring a
small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%package        doc
Summary:        Documentation for %{name}

%description    doc
The %{name}-doc package contains documentation for the %{name} library.

%prep -a
sed -i 's/pthread-stubs //' configure.ac
export LC_ALL=C
autoreconf -ivf

%install -a
mkdir -p %{buildroot}%{_libdir}/pkgconfig
sed 's,@libdir@,%{_libdir},;s,@prefix@,%{_prefix},;s,@exec_prefix@,%{_exec_prefix},' %{S:1} \
    > %{buildroot}%{_libdir}/pkgconfig/pthread-stubs.pc

%files
%license COPYING
%{_libdir}/libxcb*.so.*

%files devel
%{_includedir}/xcb
%{_libdir}/*.so
%{_libdir}/pkgconfig/pthread-stubs.pc
%{_libdir}/pkgconfig/xcb-composite.pc
%{_libdir}/pkgconfig/xcb-damage.pc
%{_libdir}/pkgconfig/xcb-dbe.pc
%{_libdir}/pkgconfig/xcb-dpms.pc
%{_libdir}/pkgconfig/xcb-dri2.pc
%{_libdir}/pkgconfig/xcb-dri3.pc
%{_libdir}/pkgconfig/xcb-glx.pc
%{_libdir}/pkgconfig/xcb-present.pc
%{_libdir}/pkgconfig/xcb-randr.pc
%{_libdir}/pkgconfig/xcb-record.pc
%{_libdir}/pkgconfig/xcb-render.pc
%{_libdir}/pkgconfig/xcb-res.pc
%{_libdir}/pkgconfig/xcb-screensaver.pc
%{_libdir}/pkgconfig/xcb-shape.pc
%{_libdir}/pkgconfig/xcb-shm.pc
%{_libdir}/pkgconfig/xcb-sync.pc
%{_libdir}/pkgconfig/xcb-xf86dri.pc
%{_libdir}/pkgconfig/xcb-xfixes.pc
%{_libdir}/pkgconfig/xcb-xinerama.pc
%{_libdir}/pkgconfig/xcb-xinput.pc
%{_libdir}/pkgconfig/xcb-xkb.pc
%{_libdir}/pkgconfig/xcb-xselinux.pc
%{_libdir}/pkgconfig/xcb-xtest.pc
%{_libdir}/pkgconfig/xcb-xv.pc
%{_libdir}/pkgconfig/xcb-xvmc.pc
%{_libdir}/pkgconfig/xcb.pc

%files doc
%doc NEWS README.md
%{_mandir}/man3/*.3*
%doc %{_datadir}/doc/*

%changelog
%autochangelog
