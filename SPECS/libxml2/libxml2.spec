# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libxml2
Version:        2.14.5
Release:        %autorelease
Summary:        A Library to Manipulate XML Files
License:        MIT
URL:            https://gitlab.gnome.org/GNOME/libxml2
VCS:            git:https://gitlab.gnome.org/nwellnhof/libxml2.git
#!RemoteAsset:  sha256:03d006f3537616833c16c53addcdc32a0eb20e55443cba4038307e3fa7d8d44b
Source:         https://download.gnome.org/sources/libxml2/2.14/libxml2-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --enable-shared
BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --disable-static
BuildOption(conf):  --docdir=%{_docdir}/%{name}
BuildOption(conf):  --with-history
BuildOption(conf):  --enable-ipv6
BuildOption(conf):  --with-sax1
BuildOption(conf):  --with-regexps
BuildOption(conf):  --with-threads
BuildOption(conf):  --with-reader
BuildOption(conf):  --with-ftp
BuildOption(conf):  --with-http
BuildOption(conf):  --with-legacy
BuildOption(conf):  --with-python=%{__python3}

BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)

%description
The XML C library was developed for the GNOME project. It is used by many
programs to load, save, and manipulate any kind of XML files.
This package contains the core runtime library and command-line tools.

%package        devel
Summary:        Development files for libxml2
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glibc-devel
Requires:       pkgconfig(liblzma)
Requires:       pkgconfig(zlib)

%description    devel
This subpackage contains header files for developing applications that
want to make use of libxml2.

%package     -n python-%{name}
Summary:        Python bindings for the libxml2 library
BuildRequires:  pkgconfig(python3)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-%{name} = %{version}-%{release}
Provides:       python3-%{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-python3 = %{version}-%{release}

%description -n python-%{name}
The python-%{name} package contains a Python module that permits
applications written in the Python programming language to use the
interface supplied by the libxml2 library to manipulate XML files.

This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DTDs, either
at parse time or later once the document has been modified.

%install -a
ln -s libxml2/libxml %{buildroot}%{_includedir}/libxml
rm -f %{buildroot}%{_docdir}/%{name}/Copyright
%fdupes %{buildroot}%{_datadir}

%files
%license Copyright
%doc %{_docdir}/%{name}/
%{_bindir}/xmllint
%{_bindir}/xmlcatalog
%{_mandir}/man1/xmllint.1*
%{_mandir}/man1/xmlcatalog.1*
%{_libdir}/libxml2.so.*

%files devel
%{_bindir}/xml2-config
%{_includedir}/libxml*
%{_libdir}/libxml2.so
%{_libdir}/pkgconfig/libxml-2.0.pc
%{_libdir}/cmake/
%{_mandir}/man1/xml2-config.1*
%{_datadir}/gtk-doc/

%files -n python-libxml2
%doc doc/*.py
%{python3_sitearch}/*.so
%{python3_sitelib}/*.py
%{python3_sitelib}/__pycache__/*.pyc

%changelog
%autochangelog
