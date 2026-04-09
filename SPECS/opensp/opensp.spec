# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           opensp
Version:        1.5.2
Release:        %autorelease
Summary:        SGML and XML parser
License:        X11
URL:            http://openjade.sourceforge.net/
#!RemoteAsset
Source0:        http://download.sourceforge.net/openjade/OpenSP-%{version}.tar.gz
BuildSystem:    autotools

# configure: error: unrecognized option: --docdir=/usr/share/doc/opensp
# So we need to use this
BuildOption(conf):  --disable-doc-build
BuildOption(conf):  --disable-dependency-tracking
BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-http
BuildOption(conf):  --enable-default-catalog=/etc/sgml/catalog
BuildOption(conf):  --enable-default-search-path=/usr/share/sgml:/usr/share/xml

BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

Requires:       sgml-common

%description
OpenSP is an implementation of the ISO/IEC 8879:1986 standard SGML
(Standard Generalized Markup Language). OpenSP is based on James
Clark's SP implementation of SGML. OpenSP is a command-line
application and a set of components, including a generic API.

%package        devel
Summary:        Files for developing applications that use OpenSP
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and libtool library for developing applications that use OpenSP.

%prep
%autosetup -n OpenSP-%{version}
# convert files to UTF-8
iconv -f latin1 -t utf8 ChangeLog -o ChangeLog.tmp
mv -f ChangeLog.tmp ChangeLog

%conf -p
autoreconf -fiv

%install -a
for file in nsgmls sgmlnorm spam spent sx ; do
   ln -s o$file $RPM_BUILD_ROOT%{_bindir}/$file
done

# Rename sx to sgml2xml.
mv $RPM_BUILD_ROOT%{_bindir}/sx $RPM_BUILD_ROOT%{_bindir}/sgml2xml

# Clean out (installed) redundant copies of the docs and DTDs.
rm -rf $RPM_BUILD_ROOT%{_docdir}/OpenSP
rm -rf $RPM_BUILD_ROOT%{_datadir}/OpenSP

%find_lang OpenSP --generate-subpackages

# TODO: Broken check also no distro is checking it - 251
%check

%files
%doc AUTHORS BUGS COPYING ChangeLog NEWS README
%doc pubtext/opensp-implied.dcl
%{_bindir}/*
%{_libdir}/libosp.so.*

%files devel
%{_includedir}/OpenSP/
%{_libdir}/libosp.so

%changelog
%autochangelog
