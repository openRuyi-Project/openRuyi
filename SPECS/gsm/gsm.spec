# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target tst

Name:           gsm
Version:        1.0.23
Release:        %autorelease
Summary:        Shared libraries for GSM speech compressor
License:        tu-berlin-2.0
URL:            https://www.quut.com/gsm/
# VCS: No VCS link available
#!RemoteAsset:  sha256:8b7591a85ac9adce858f2053005e6b2eb20c23b8b8a868dffb2969645fa323c0
Source0:        https://www.quut.com/gsm/gsm-%{version}.tar.gz
BuildSystem:    autotools

# the makefile didn't install some files.
Patch0:         0001-fix-makefile-install.patch

BuildOption(build):  all
BuildOption(build):  LDFLAGS="%{build_ldflags}"
BuildOption(install):  INSTALL_ROOT=%{buildroot}%{_prefix}
BuildOption(install):  GSM_INSTALL_INC=%{buildroot}%{_includedir}/gsm
BuildOption(install):  GSM_INSTALL_LIB=%{buildroot}%{_libdir}

BuildRequires:  gcc
BuildRequires:  make

%description
Contains runtime shared libraries for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding.

%package        devel
Summary:        Header files and development libraries for libgsm
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Contains header files and development libraries for libgsm.

# No configure.
%conf

%install -p
mkdir -p %{buildroot}{%{_bindir},%{_includedir}/gsm,%{_libdir},%{_mandir}/{man1,man3}}

%install -a
ln -s gsm/gsm.h %{buildroot}%{_includedir}/

echo ".so toast.1" > %{buildroot}%{_mandir}/man1/tcat.1
echo ".so toast.1" > %{buildroot}%{_mandir}/man1/untoast.1

%files
%license COPYRIGHT
%doc ChangeLog MACHINES README
%{_libdir}/libgsm.so.*
%{_bindir}/tcat
%{_bindir}/toast
%{_bindir}/untoast
%{_mandir}/man1/tcat.1*
%{_mandir}/man1/toast.1*
%{_mandir}/man1/untoast.1*

%files devel
%dir %{_includedir}/gsm
%{_includedir}/gsm/gsm.h
%{_includedir}/gsm.h
%{_libdir}/libgsm.so
%{_mandir}/man3/gsm.3*
%{_mandir}/man3/gsm_explode.3*
%{_mandir}/man3/gsm_option.3*
%{_mandir}/man3/gsm_print.3*

%changelog
%autochangelog
