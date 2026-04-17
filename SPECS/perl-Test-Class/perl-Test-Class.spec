# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Test-Class
Version:        0.52
Release:        %autorelease
Summary:        Easily create test classes in an xUnit/JUnit style
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-Class
#!RemoteAsset:  sha256:40c1b1d388f0a8674769c27529f0cc3634ca0fd9d8f72b196c0531611934bc82
Source0:        https://cpan.metacpan.org/authors/id/S/SZ/SZABGAB/Test-Class-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Attribute::Handlers) >= 0.77
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File) >= 1.09
BuildRequires:  perl(MRO::Compat) >= 0.11
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Storable) >= 2.04
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Builder) >= 0.78
BuildRequires:  perl(Test::Builder::Tester) >= 1.02
BuildRequires:  perl(Test::Exception) >= 0.25
BuildRequires:  perl(Test::More) >= 0.78
BuildRequires:  perl(Test::Simple) >= 0.78
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(Attribute::Handlers) >= 0.77
Requires:       perl(MRO::Compat) >= 0.11
Requires:       perl(Storable) >= 2.04
Requires:       perl(Test::Builder) >= 0.78
Requires:       perl(Test::Builder::Tester) >= 1.02
Requires:       perl(Test::Simple) >= 0.78

%description
Test::Class provides a simple way of creating classes and objects to test
your code in an xUnit style.

%prep
%setup -q -n Test-Class-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license

%changelog
%autochangelog
