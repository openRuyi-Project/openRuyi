# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           deltarpm
Version:        3.6.5
Release:        %autorelease
Summary:        Create deltas between rpms
License:        BSD-3-Clause
URL:            https://github.com/rpm-software-management/deltarpm
#!RemoteAsset
Source0:        https://github.com/rpm-software-management/deltarpm/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

# add build python and fix install dir.
Patch0:         0001-fix-install-dir.patch

BuildOption(install):  prefix=%{_prefix}
BuildOption(install):  mandir=%{_mandir}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(zlib)

%description
A deltarpm contains the difference between an old and a new version of a rpm.

%package     -n drpmsync
Summary:        Sync a file tree with deltarpms
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n drpmsync
Tool to sync a file tree with deltarpms.

%package     -n deltaiso
Summary:        Create deltas between isos containing rpms
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n deltaiso
Tools for creating and using deltaisos.

%package     -n python-deltarpm
Summary:        Python bindings for deltarpm
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-deltarpm
%python_provide python3-deltarpm

%description -n python-deltarpm
Python 3 bindings for deltarpm.

# No configure.
%conf

%check
# No tests here.

%files
%license LICENSE.BSD
%doc README NEWS
%{_bindir}/applydeltarpm
%{_bindir}/combinedeltarpm
%{_bindir}/makedeltarpm
%{_bindir}/rpmdumpheader
%{_mandir}/man8/applydeltarpm.8*
%{_mandir}/man8/combinedeltarpm.8*
%{_mandir}/man8/makedeltarpm.8*

%files -n deltaiso
%{_bindir}/applydeltaiso
%{_bindir}/fragiso
%{_bindir}/makedeltaiso
%{_mandir}/man8/applydeltaiso.8*
%{_mandir}/man8/fragiso.8*
%{_mandir}/man8/makedeltaiso.8*

%files -n drpmsync
%{_bindir}/drpmsync
%{_mandir}/man8/drpmsync.8*

%files -n python-deltarpm
%{python3_sitearch}/deltarpm.py
%{python3_sitearch}/_deltarpmmodule.so

%changelog
%autochangelog
