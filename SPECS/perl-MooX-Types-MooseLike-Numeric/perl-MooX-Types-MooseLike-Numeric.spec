# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-MooX-Types-MooseLike-Numeric
Version:        1.03
Release:        %autorelease
Summary:        Moo types for numbers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/MooX-Types-MooseLike-Numeric
#!RemoteAsset:  sha256:16adeb617b963d010179922c2e4e8762df77c75232e17320b459868c4970c44b
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATEU/MooX-Types-MooseLike-Numeric-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moo) >= 1.004002
BuildRequires:  perl(MooX::Types::MooseLike) >= 0.23
BuildRequires:  perl(Test::Fatal) >= 0.003
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(MooX::Types::MooseLike) >= 0.23

%description
A set of numeric types to be used in Moo-based classes. Adapted from
MooseX::Types::Common::Numeric

%prep
%setup -q -n MooX-Types-MooseLike-Numeric-%{version}

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
