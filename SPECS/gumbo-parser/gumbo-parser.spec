# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gumbo-parser
Version:        0.13.2
Release:        %autorelease
Summary:        A HTML5 parser
License:        Apache-2.0
URL:            https://codeberg.org/gumbo-parser/gumbo-parser
#!RemoteAsset:  sha256:dbdc159dc8e5c6f3f254e50bce689dd9e439064ff06c165d5653410a5714ab66
Source0:        https://codeberg.org/gumbo-parser/gumbo-parser/archive/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --docdir=%{_pkgdocdir}
BuildOption(check):  CXXFLAGS="%{build_cxxflags} -std=gnu++17"

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  pkgconfig(gtest)
BuildRequires:  doxygen
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-rpm-macros

%description
Gumbo is an implementation of the HTML5 parsing algorithm implemented as
a pure C99 library with no outside dependencies.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for gumbo-parser.

%package     -n python-gumbo
Summary:        Python bindings to %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildArch:      noarch
Provides:       python3-gumbo
%python_provide python3-gumbo

%description -n python-gumbo
Python bindings to gumbo-parser.

%conf -p
./autogen.sh
doxygen -u Doxyfile

%build -a
doxygen Doxyfile
%{__python3} setup.py build

%install -a
install -d %{buildroot}%{_mandir}/man3
install -m 644 docs/man/man3/*.3 %{buildroot}%{_mandir}/man3/

install -d %{buildroot}%{_pkgdocdir}
cp -r docs/html %{buildroot}%{_pkgdocdir}
install -m 644 doc/*.md %{buildroot}%{_pkgdocdir}

%{__python3} setup.py install --root=%{buildroot} --skip-build --optimize=1

%files
%license doc/COPYING
%doc %{_pkgdocdir}/
%exclude %{_pkgdocdir}/html
%exclude %{_pkgdocdir}/*.md
%{_libdir}/*.so.*

%files devel
%doc %{_pkgdocdir}/html
%doc %{_pkgdocdir}/*.md
%{_includedir}/gumbo.h
%{_includedir}/tag_enum.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/gumbo.pc
%{_mandir}/man3/*.3*

%files -n python-gumbo
%{python3_sitelib}/gumbo/
%{python3_sitelib}/gumbo-*.egg-info

%changelog
%autochangelog
