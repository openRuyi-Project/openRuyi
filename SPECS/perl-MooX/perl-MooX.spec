# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-MooX
Version:        0.101
Release:        %autorelease
Summary:        Using Moo and MooX:: packages the most lazy way
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX
#!RemoteAsset:  sha256:2ff91a656e78aae0aca42293829d7a7e5acb9bf22b0401635b2ab6c870de32d5
Source0:        https://cpan.metacpan.org/authors/id/G/GE/GETTY/MooX-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Runtime) >= 0.013
BuildRequires:  perl(Moo) >= 0.091004
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(Import::Into)
Requires:       perl(Data::OptList) >= 0.107

%description
Using Moo and MooX:: packages the most lazy way

%prep
%setup -q -n MooX-%{version}

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
