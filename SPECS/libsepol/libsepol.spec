# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libsepol
Version:        3.8.1
Release:        %autorelease
Summary:        SELinux binary policy manipulation library
License:        LGPL-2.1-or-later
URL:            https://github.com/SELinuxProject/selinux/wiki/Releases
#!RemoteAsset
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
BuildRequires:  flex
BuildRequires:  pkgconfig
BuildOption(install):  LIBDIR="%{_libdir}" SHLIBDIR="%{_libdir}"
BuildSystem:    autotools



%description
libsepol provides an API for the manipulation of SELinux binary
policies. It is used by checkpolicy (the policy compiler) and similar
tools, as well as by programs like load_policy that need to perform
specific transformations on binary policies such as customizing
policy boolean settings.

%package utils
Summary:        SELinux binary policy manipulation tools

%description utils
libsepol provides an API for the manipulation of SELinux binary
policies. It is used by checkpolicy (the policy compiler) and similar
tools, as well as by programs like load_policy that need to perform
specific transformations on binary policies such as customizing
policy boolean settings.

%package devel
Summary:        Development files for SELinux's binary policy manipulation library
Requires:       %{name} = %{version}
Requires:       glibc-devel

%description devel
The libsepol-devel package contains the libraries and header files
needed for developing applications that manipulate binary SELinux
policies.

%package static
Summary:        Static archives for SELinux's binary policy manipulation library
Requires:       libsepol-devel = %{version}

%description static
The libsepol-devel-static package contains the static libraries
needed for developing applications that manipulate binary SELinux
policies.

# no configure script
%conf
:

%files utils
%defattr(-,root,root)
%{_bindir}/chkcon
%{_bindir}/sepol_check_access
%{_bindir}/sepol_compute_av
%{_bindir}/sepol_compute_member
%{_bindir}/sepol_compute_relabel
%{_bindir}/sepol_validate_transition
%{_mandir}/man8/*.8%{ext_man}

%files
%defattr(-,root,root)
%{_libdir}/libsepol.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libsepol.so
%{_mandir}/man3/*.3%{ext_man}
%{_includedir}/sepol/
%{_libdir}/pkgconfig/libsepol.pc

%files static
%defattr(-,root,root)
%{_libdir}/libsepol.a

%changelog
%{?autochangelog}
