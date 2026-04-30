# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Class-Load
Version:        0.25
Release:        %autorelease
Summary:        Working (require "Class::Name") and more
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Class-Load
#!RemoteAsset:  sha256:2a48fa779b5297e56156380e8b32637c6c58decb4f4a7f3c7350523e11275f8f
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Class-Load-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::OptList) >= 0.110
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Implementation) >= 0.04
BuildRequires:  perl(Module::Runtime) >= 0.012
BuildRequires:  perl(Package::Stash) >= 0.14
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
Requires:       perl(Data::OptList) >= 0.110
Requires:       perl(Module::Implementation) >= 0.04
Requires:       perl(Module::Runtime) >= 0.012
Requires:       perl(Package::Stash) >= 0.14

%description
require EXPR only accepts Class/Name.pm style module names, not
Class::Name. How frustrating! For that, we provide load_class
'Class::Name'.

%prep
%setup -q -n Class-Load-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CONTRIBUTING Changes README
%license LICENSE

%changelog
%autochangelog
