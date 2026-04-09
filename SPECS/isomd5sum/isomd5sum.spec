# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           isomd5sum
Version:        1.2.5
Release:        %autorelease
Summary:        Utilities for working with md5sum implanted in ISO images
License:        GPL-2.0-or-later
URL:            https://github.com/rhinstaller/isomd5sum
#!RemoteAsset
Source0:        https://github.com/rhinstaller/isomd5sum/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(install):  PYTHON=%{__python3}
BuildOption(install):  DESTDIR=%{buildroot}
BuildOption(install):  install-bin install-devel install-python
BuildOption(build):  CFLAGS="%{optflags} -fPIC $(python3-config --includes)"
BuildOption(build):  LDFLAGS="%{build_ldflags}"
BuildOption(build):  PYTHON=%{__python3}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(python3)

%description
The isomd5sum package contains utilities for implanting and verifying
an md5sum implanted into an ISO9660 image.

%package        devel
Summary:        Development headers and library for using isomd5sum
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This contains header files and a library for working with the isomd5sum
implanting and checking.

%package     -n python-isomd5sum
Summary:        Python bindings for isomd5sum
Requires:       %{name} = %{version}-%{release}
Provides:       python3-isomd5sum
%python_provide python3-isomd5sum

%description -n python-isomd5sum
This package contains python bindings for isomd5sum.

# No configure.
%conf

%check
# skip tests as we have no mkisofs.

%files
%license COPYING
%{_bindir}/implantisomd5
%{_bindir}/checkisomd5
%{_mandir}/man*/*

%files devel
%{_includedir}/*.h
%{_libdir}/*.a
%{_datadir}/pkgconfig/isomd5sum.pc

%files -n python-isomd5sum
%{python3_sitearch}/pyisomd5sum.so

%changelog
%autochangelog
