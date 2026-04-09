# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-DateTime-Format-Builder
Version:        0.83
Release:        %autorelease
Summary:        Create DateTime parser classes and objects
License:        Artistic-2.0
URL:            https://metacpan.org/dist/DateTime-Format-Builder
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-Builder-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime) >= 1.00
BuildRequires:  perl(DateTime::Format::Strptime) >= 1.04
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Params::Validate) >= 0.72
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(warnings)

Requires:       perl(DateTime) >= 1.00
Requires:       perl(DateTime::Format::Strptime) >= 1.04
Requires:       perl(Params::Validate) >= 0.72

%description
DateTime::Format::Builder creates DateTime parsers. Many string formats of
dates and times are simple and just require a basic regular expression to
extract the relevant information. Builder provides a simple way to do this
without writing reams of structural code.

%prep
%setup -q -n DateTime-Format-Builder-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc azure-pipelines.yml Changes CODE_OF_CONDUCT.md CONTRIBUTING.md perlcriticrc perltidyrc README.md tidyall.ini

%changelog
%autochangelog
