# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libglvnd
Version:        1.7.0
Release:        %autorelease
Summary:        The GL Vendor-Neutral Dispatch library
License:        MIT AND BSD-3-Clause AND GPL-3.0-or-later
URL:            https://gitlab.freedesktop.org/glvnd/libglvnd
#!RemoteAsset
Source:         https://gitlab.freedesktop.org/glvnd/libglvnd/-/archive/v%{version}/libglvnd-v%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dasm=disabled
BuildOption(conf):  -Dtls=true
BuildOption(conf):  -Ddispatch-tls=true
BuildOption(conf):  -Dx11=enabled
BuildOption(conf):  -Dglx=enabled
BuildOption(conf):  -Degl=true
BuildOption(conf):  -Dgles1=true
BuildOption(conf):  -Dgles2=true
BuildOption(conf):  -Dheaders=true

BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  meson

%description
libglvnd is an implementation of the vendor-neutral dispatch layer for
arbitrating OpenGL API calls between multiple vendors on a per-screen basis.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-egl = %{version}-%{release}
Requires:       %{name}-core-devel = %{version}-%{release}
Requires:       libX11-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        core-devel
Summary:        Core development files for %{name}

%description    core-devel
The %{name}-core-devel package is a bootstrap trick for Mesa.

%package        egl
Summary:        EGL support for libglvnd
Requires:       %{name} = %{version}-%{release}

%description    egl
libEGL are the common dispatch interface for the EGL API.

# avoid require a running xorg server.
%prep -a
sed -i 's/if with_glx/if false/g' tests/meson.build

%install -a
mkdir -p %{buildroot}%{_sysconfdir}/glvnd/egl_vendor.d/
mkdir -p %{buildroot}%{_datadir}/glvnd/egl_vendor.d/
mkdir -p %{buildroot}%{_sysconfdir}/egl/egl_external_platform.d/
mkdir -p %{buildroot}%{_datadir}/egl/egl_external_platform.d/

%files
%doc README.md
%dir %{_sysconfdir}/glvnd/
%dir %{_datadir}/glvnd/
%{_libdir}/libGLdispatch.so.0*
%{_libdir}/libOpenGL.so.0*
%{_libdir}/libGLES*.so.*
%{_libdir}/libGL.so.*
%{_libdir}/libGLX.so.*

%files egl
%dir %{_sysconfdir}/glvnd/egl_vendor.d/
%dir %{_datadir}/glvnd/egl_vendor.d/
%dir %{_sysconfdir}/egl/
%dir %{_sysconfdir}/egl/egl_external_platform.d/
%dir %{_datadir}/egl/
%dir %{_datadir}/egl/egl_external_platform.d/
%{_libdir}/libEGL*.so.*

%files core-devel
%dir %{_includedir}/glvnd/
%{_includedir}/glvnd/*.h
%{_libdir}/pkgconfig/libglvnd.pc

%files devel
%dir %{_includedir}/EGL/
%dir %{_includedir}/GL/
%dir %{_includedir}/GLES/
%dir %{_includedir}/GLES2/
%dir %{_includedir}/GLES3/
%dir %{_includedir}/KHR/
%{_includedir}/EGL/*.h
%{_includedir}/GL/*.h
%{_includedir}/GLES/*.h
%{_includedir}/GLES2/*.h
%{_includedir}/GLES3/*.h
%{_includedir}/KHR/*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/gl*.pc
%{_libdir}/pkgconfig/egl.pc
%{_libdir}/pkgconfig/opengl.pc

%changelog
%autochangelog
