# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# No python docs for now, sorry!
# Change this to 1 once we have python-sphinx
%bcond sphinx 0

Name:           libcomps
Version:        0.1.23
Release:        %autorelease
Summary:        Comps XML file manipulation library
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/libcomps
#!RemoteAsset
Source:         %{url}/archive/%{version}/libcomps-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DPYTHON_DESIRED:STRING=3 libcomps

BuildRequires:  cmake
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(check)

%description
Libcomps is library for structure-like manipulation with content of
comps XML files. Supports read/write XML file, structure(s) modification.

%package        devel
Summary:        Development files for libcomps library
Requires:       %{name} = %{version}-%{release}

%description    devel
Development files for libcomps library.

%package        doc
Summary:        Documentation files for libcomps library
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  doxygen

%description    doc
Documentation files for libcomps library.

%package -n python-%{name}
Summary:        Python bindings for libcomps library
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  make
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
Requires:       %{name} = %{version}-%{release}

%description -n python-%{name}
Python3 bindings for libcomps library.

%if %{with sphinx}
%package -n python-%{name}-doc
Summary:        Documentation files for python bindings libcomps library
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
BuildRequires:  python3-sphinx

%description -n python-%{name}-doc
Documentation files for python bindings libcomps library.
%endif

%build -a
%cmake_build -t docs
%if %{with sphinx}
%cmake_build -t pydocs
%endif

%install -a
%if %{with sphinx}
mkdir -p %{buildroot}%{_datadir}/doc/python-libcomps/
rm %{__cmake_builddir}/src/python/docs/html/.doctrees/environment.pickle
cp -a %{__cmake_builddir}/src/python/docs/html %{buildroot}%{_datadir}/doc/python-libcomps/
%endif

%files
%{_libdir}/libcomps.so.*
%doc README.md
%license COPYING

%files devel
%{_libdir}/libcomps.so
%{_libdir}/pkgconfig/libcomps.pc
%{_includedir}/libcomps/

%files doc
%{_datadir}/doc/*

%files -n python-%{name}
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-%{version}-py%{python3_version}.egg-info

%if %{with sphinx}
%files -n python-%{name}-doc
%{_datadir}/doc/python-%{name}/html
%endif

%changelog
%{?autochangelog}
