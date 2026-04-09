# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-DateTime-Format-Strptime
Version:        1.79
Release:        %autorelease
Summary:        Parse and format strp and strf time patterns
License:        Artistic-2.0
URL:            https://metacpan.org/dist/DateTime-Format-Strptime
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-Strptime-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime) >= 1.00
BuildRequires:  perl(DateTime::Locale) >= 1.30
BuildRequires:  perl(DateTime::Locale::Base)
BuildRequires:  perl(DateTime::Locale::FromData)
BuildRequires:  perl(DateTime::TimeZone) >= 2.09
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Params::ValidationCompiler)
BuildRequires:  perl(parent)
BuildRequires:  perl(Specio) >= 0.33
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Exporter)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

Requires:       perl(DateTime) >= 1.00
Requires:       perl(DateTime::Locale) >= 1.30
Requires:       perl(DateTime::TimeZone) >= 2.09
Requires:       perl(Specio) >= 0.33

%description
This module implements most of strptime(3), the POSIX function that is the
reverse of strftime(3), for DateTime. While strftime takes a DateTime and a
pattern and returns a string, strptime takes a string and a pattern and
returns the DateTime object associated.

%prep
%setup -q -n DateTime-Format-Strptime-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc azure-pipelines.yml bench Changes CODE_OF_CONDUCT.md CONTRIBUTING.md perlcriticrc perltidyrc precious.toml README.md

%changelog
%autochangelog
