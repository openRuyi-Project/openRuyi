# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define libsepol_ver 3.10

Name:           libselinux
Version:        3.10
Release:        %autorelease
Summary:        SELinux runtime library and utilities
License:        LicenseRef-openRuyi-Public-Domain
URL:            https://github.com/SELinuxProject/selinux/wiki/Releases
#!RemoteAsset
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        libselinux.keyring
Source3:        selinux-ready
BuildSystem:    autotools

Patch0:         readv-proto.patch
Patch1:         skip_cycles.patch
# Make linking working even when default pkg-config doesn’t provide -lpython<ver>
Patch2:         python3.8-compat.patch
Patch3:         swig4_moduleimport.patch

BuildRequires:  libsepol-devel >= %{libsepol_ver}
BuildRequires:  libsepol-static >= %{libsepol_ver}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  python3
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  swig

BuildOption(build):  LIBDIR="%{_libdir}" CC="%__cc"
BuildOption(build):  CFLAGS="%{optflags} -fno-semantic-interposition -ffat-lto-objects"
BuildOption(build):  USE_PCRE2=y
BuildOption(install):  LIBDIR="%{_libdir}"
BuildOption(install):  SHLIBDIR="%{_libdir}"
BuildOption(install):  BINDIR="%{_bindir}"
BuildOption(install):  SBINDIR="%{_sbindir}"
BuildOption(install):  PIP_NO_BUILD_ISOLATION=0
BuildOption(install):  all install-pywrap

%description
libselinux provides an interface to get and set process and file
security contexts and to obtain security policy decisions.

%package     -n selinux-tools
Summary:        SELinux command-line utilities
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libselinux-utils = %{version}-%{release}

%description -n selinux-tools
Security-enhanced Linux is a feature of the kernel and some
utilities that implement mandatory access control policies, such as
Type Enforcement, Role-based Access Control and Multi-Level
Security.

This subpackage contains utilities to inspect and administer the
system's SELinux state.

%package        devel
Summary:        Development files for the SELinux runtime library
Requires:       glibc-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
libselinux provides an interface to get and set process and file
security contexts and to obtain security policy decisions.

This package contains the development files, which are
necessary to develop your own software using libselinux.

%package        static
Summary:        Static archives for the SELinux runtime
Requires:       libselinux-devel = %{version}-%{release}
Requires:       pkgconfig(libpcre2-8)
Requires:       pkgconfig(libsepol)

%description    static
libselinux provides an interface to get and set process and file
security contexts and to obtain security policy decisions.

This package contains the static development files, which are
necessary to develop your own software using libselinux.

%package     -n python-libselinux
Summary:        SELinux python bindings for libselinux
Provides:       python3-libselinux = %{version}-%{release}
%{?python_provide:%python_provide python3-libselinux}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python-libselinux
The libselinux-python package contains python 3 bindings for developing
SELinux applications.

# no configure scripts
%conf

%build -a
%make_build pywrap

%install -p
mkdir -p %{buildroot}/%{_lib}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_sbindir}

%install -a
mv %{buildroot}%{_sbindir}/getdefaultcon %{buildroot}%{_sbindir}/selinuxdefcon
mv %{buildroot}%{_sbindir}/getconlist %{buildroot}%{_sbindir}/selinuxconlist
install -m 0755 %{SOURCE3} %{buildroot}%{_sbindir}/selinux-ready

# No tests.
%check

%files -n selinux-tools
%{_sbindir}/avcstat
%{_sbindir}/getenforce
%{_sbindir}/getpolicyload
%{_sbindir}/getsebool
%{_sbindir}/matchpathcon
%{_sbindir}/selabel_digest
%{_sbindir}/selabel_lookup
%{_sbindir}/selinux_check_access
%{_sbindir}/selabel_compare
%{_sbindir}/selabel_lookup_best_match
%{_sbindir}/selabel_partial_match
%{_sbindir}/selinuxconlist
%{_sbindir}/selinuxdefcon
%{_sbindir}/selinuxenabled
%{_sbindir}/setenforce
%{_sbindir}/togglesebool
%{_sbindir}/selinux-ready
%{_sbindir}/selinuxexeccon
%{_sbindir}/sefcontext_compile
%{_sbindir}/compute_*
%{_sbindir}/getfilecon
%{_sbindir}/getpidcon
%{_sbindir}/policyvers
%{_sbindir}/setfilecon
%{_sbindir}/getseuser
%{_sbindir}/selinux_check_securetty_context
%{_sbindir}/selabel_get_digests_all_partial_matches
%{_sbindir}/validatetrans
%{_sbindir}/getpidprevcon
%{_mandir}/man5/*
%{_mandir}/man8/*

%files
%{_libdir}/libselinux.so.*

%files devel
%{_libdir}/libselinux.so
%{_includedir}/selinux/
%{_mandir}/man3/*
%{_libdir}/pkgconfig/libselinux.pc

%files static
%{_libdir}/libselinux.a

%files -n python-libselinux
%{python3_sitearch}/selinux/
%{python3_sitearch}/selinux-%{version}*
%{python3_sitearch}/_selinux*

%changelog
%autochangelog
