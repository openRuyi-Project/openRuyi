# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-XML-LibXSLT
Version:        2.003000
Release:        %autorelease
Summary:        Interface to the GNOME libxslt library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/XML-LibXSLT
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/S/SH/SHLOMIF/XML-LibXSLT-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.14.0
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path) >= 2.06
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::LibXML) >= 1.70
# Manual
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(libxml-2.0)

Requires:       perl(File::Path) >= 2.06
Requires:       perl(XML::LibXML) >= 1.70

%description
This module is an interface to the GNOME project's libxslt. This is an
extremely good XSLT engine, highly compliant and also very fast. I have
tests showing this to be more than twice as fast as Sablotron.

%prep
%setup -q -n XML-LibXSLT-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
