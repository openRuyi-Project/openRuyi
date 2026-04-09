# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-DateTime-Locale
Version:        1.45
Release:        %autorelease
Summary:        Localization support for DateTime.pm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/DateTime-Locale
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/DateTime-Locale-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.4
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Dist::CheckConflicts) >= 0.02
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(namespace::autoclean) >= 0.19
BuildRequires:  perl(Params::ValidationCompiler) >= 0.13
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::File::ShareDir::Dist)
BuildRequires:  perl(Test::More) >= 1.302015
BuildRequires:  perl(Test2::Plugin::NoWarnings)
BuildRequires:  perl(Test2::Plugin::UTF8)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Manual
BuildRequires:  perl(File::ShareDir::Install)

Requires:       perl(Dist::CheckConflicts) >= 0.02
Requires:       perl(List::Util) >= 1.45
Requires:       perl(namespace::autoclean) >= 0.19
Requires:       perl(Params::ValidationCompiler) >= 0.13

%description
DateTime::Locale is primarily a factory for the various locale subclasses.
It also provides some functions for getting information on all the
available locales.

%prep
%setup -q -n DateTime-Locale-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.cldr mise.toml perlcriticrc perltidyrc precious.toml README.md

%changelog
%autochangelog
