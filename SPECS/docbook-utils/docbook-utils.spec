# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# I know this does not work but we don't have texlive yet
# So we disable & exclude anything related to pdf for now
# Change to 1 to enable building pdf related - 251
%bcond pdf 0

Name:           docbook-utils
Version:        0.6.15
Release:        %autorelease
Summary:        Shell scripts for managing DocBook documents
License:        GPL-2.0-or-later
URL:            https://github.com/devexp-db/docbook-utils
#!RemoteAsset
Source0:        https://github.com/devexp-db/docbook-utils/releases/download/v%{version}/docbook-utils-%{version}.tar.xz
BuildArch:      noarch
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  perl-SGMLSpm
BuildRequires:  sgml-common
BuildRequires:  openjade
BuildRequires:  docbook-style-dsssl

Requires:       docbook-style-dsssl
Requires:       docbook-dtds
Requires:       perl-SGMLSpm
Requires:       openjade

%description
This package contains scripts are for easy conversion from DocBook
files to other formats (for example, HTML, RTF, and PostScript), and
for comparing SGML files.

%if %{with pdf}
%package        pdf
Requires:       texlive-jadetex >= 7
Requires:       docbook-utils = %{version}
Requires:       tex(dvips)
Requires:       texlive-collection-fontsrecommended
Requires:       texlive-collection-htmlxml
License:        GPL-1.0-or-later
Obsoletes:      stylesheets-db2pdf <= %{version}-%{release}
Provides:       stylesheets-db2pdf = %{version}-%{release}
Summary:        A script for converting DocBook documents to PDF format
URL:            http://sources.redhat.com/docbook-tools/

%description    pdf
This package contains a script for converting DocBook documents to
PDF format.
%endif

%conf
# We need to write our own configure
./configure --prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir}

%install
export DESTDIR=$RPM_BUILD_ROOT
%make_install prefix=%{_prefix} mandir=%{_mandir} docdir=/tmp
for util in html rtf; do
  ln -s docbook2$util %{buildroot}%{_bindir}/db2$util
  ln -s jw.1.gz %{buildroot}%{_mandir}/man1/db2$util.1
done

%if %{with pdf}
for util in dvi pdf ps; do
  ln -s docbook2$util %{buildroot}%{_bindir}/db2$util
  ln -s jw.1.gz %{buildroot}%{_mandir}/man1/db2$util.1
done
%endif

ln -s jw.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/docbook2txt.1

rm -rf $RPM_BUILD_ROOT/tmp

%files
%doc README COPYING TODO
%{_bindir}/jw
%{_bindir}/docbook2html
%{_bindir}/docbook2man
%{_bindir}/docbook2rtf
%{_bindir}/docbook2tex
%{_bindir}/docbook2texi
%{_bindir}/docbook2txt
%attr(0755,root,root) %{_bindir}/db2html
%{_bindir}/db2rtf
%{_bindir}/sgmldiff
%{_datadir}/sgml/docbook/utils-%{version}
%{_mandir}/*/db2html.*
%{_mandir}/*/db2rtf.*
%{_mandir}/*/docbook2html.*
%{_mandir}/*/docbook2rtf.*
%{_mandir}/*/docbook2man.*
%{_mandir}/*/docbook2tex.*
%{_mandir}/*/docbook2texi.*
%{_mandir}/*/docbook2txt.*
%{_mandir}/*/jw.*
%{_mandir}/*/sgmldiff.*
%{_mandir}/*/*-spec.*
# TODO: read the beginning of the file for explanation - 251
#{_mandir}/*/db2dvi.*
#{_mandir}/*/db2ps.*
%if %{without pdf}
%exclude %{_bindir}/docbook2pdf
%exclude %{_bindir}/docbook2dvi
%exclude %{_bindir}/docbook2ps
%exclude %{_mandir}/*/docbook2pdf.*
%exclude %{_mandir}/*/docbook2dvi.*
%exclude %{_mandir}/*/docbook2ps.*
%endif

%if %{with pdf}
%files pdf
%{_bindir}/docbook2pdf
%{_bindir}/docbook2dvi
%{_bindir}/docbook2ps
%{_bindir}/db2dvi
%{_bindir}/db2pdf
%{_bindir}/db2ps
%{_mandir}/*/db2pdf.*
%{_mandir}/*/docbook2pdf.*
%{_mandir}/*/docbook2dvi.*
%{_mandir}/*/docbook2ps.*
%endif

%changelog
%autochangelog
