# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-XML-SAX
Version:        1.02
Release:        %autorelease
Summary:        Simple API for XML
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/XML-SAX
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/G/GR/GRANTM/XML-SAX-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(XML::NamespaceSupport) >= 0.03
BuildRequires:  perl(XML::SAX::Base) >= 1.05

Requires:       perl(XML::NamespaceSupport) >= 0.03
Requires:       perl(XML::SAX::Base) >= 1.05

%description
XML::SAX is a SAX parser access API for Perl. It includes classes and APIs
required for implementing SAX drivers, along with a factory class for
returning any SAX parser installed on the user's system.

%prep
%setup -q -n XML-SAX-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
