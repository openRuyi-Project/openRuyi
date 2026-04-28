# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond asciidoc 0

Name:           openscap
Version:        1.4.4
Release:        %autorelease
Summary:        Open Source Libraries for SCAP Integration
License:        LGPL-2.1-or-later
URL:            http://www.open-scap.org/
VCS:            git:https://github.com/OpenSCAP/openscap
#!RemoteAsset:  sha256:25b1b046822121204e6d53d877a532c88bf7fde14b94c9c72297cd5709b03478
Source:         https://github.com/OpenSCAP/openscap/releases/download/%{version}/openscap-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DWITH_PCRE2=ON
BuildOption(conf):  -DENABLE_PERL=ON
BuildOption(conf):  -DENABLE_DOCS=ON
BuildOption(conf):  -DOPENSCAP_PROBE_UNIX_GCONF=OFF
BuildOption(conf):  -DGCONF_LIBRARY=

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  swig
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(libproc2)
%if %{with asciidoc}
BuildRequires:  asciidoc
%endif
BuildRequires:  pkgconfig(xmlsec1)
BuildRequires:  pkgconfig(xmlsec1-openssl)
BuildRequires:  pkgconfig(libcurl) >= 7.12.0
BuildRequires:  pkgconfig(bash-completion)
# for tests
BuildRequires:  perl-devel
BuildRequires:  perl-macros
BuildRequires:  perl(XML::XPath)
BuildRequires:  bzip2

Requires:       bash
Requires:       bzip2
Requires:       dbus
Requires:       glib
Requires:       acl
Requires:       libblkid
Requires:       libcap
Requires:       libselinux
Requires:       openldap
Requires:       popt
Requires:       procps
Requires:       xmlsec
Requires:       xmlsec-openssl
Requires:       curl >= 7.12.0
Requires:       rpmdevtools
Requires:       rpm-build

%description
OpenSCAP is a set of open source libraries providing an easier path
for integration of the SCAP line of standards. SCAP is a line of standards
managed by NIST with the goal of providing a standard language
for the expression of Computer Network Defense related information.

%package        devel
Summary:        Development files for %{name}
BuildRequires:  doxygen
Requires:       pkgconfig(libxml-2.0)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n python-%{name}
Summary:        Python bindings for %{name}
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python-rpm-macros
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-%{name} = %{version}-%{release}
Provides:       %{name}-python = %{version}-%{release}

%description -n python-%{name}
The %{name}-python package contains the bindings so that %{name}
libraries can be used by python.

%package     -n perl-%{name}
Summary:        Perl bindings for %{name}
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-macros
BuildRequires:  perl(XML::Parser)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-perl = %{version}-%{release}

%description -n perl-%{name}
The perl package contains the bindings so that %{name}
libraries can be used by perl.

%install -a
mkdir -p %{buildroot}%{bash_completions_dir}
mv %{buildroot}%{_sysconfdir}/bash_completion.d/* %{buildroot}%{bash_completions_dir}/

%{__python3} %{_rpmconfigdir}/openruyi/pathfix.py -i %{__python3} -p -n $RPM_BUILD_ROOT%{_bindir}/scap-as-rpm

%check
ctest -V -E sce/test_sce_in_ds.sh

%files
%license COPYING
%doc AUTHORS NEWS README.md docs/oscap-scan.cron
%if %{with asciidoc}
%doc %{_pkgdocdir}/manual/
%endif
%doc %{_pkgdocdir}/html/
%{_bindir}/*
%{_libdir}/*.so.*
%dir %{_datadir}/openscap
%dir %{_datadir}/openscap/schemas
%dir %{_datadir}/openscap/xsl
%dir %{_datadir}/openscap/cpe
%{_datadir}/openscap/schemas/*
%{_datadir}/openscap/xsl/*
%{_datadir}/openscap/cpe/*
%{bash_completions_dir}/*
%{_mandir}/man8/*

%files -n python-openscap
%{python3_sitearch}/*
%{python3_sitelib}/oscap_docker_python/*

%files -n perl-openscap
%{perl_vendorlib}/openscap_pm.pm
%{perl_vendorarch}/openscap_pm.so

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%changelog
%autochangelog
