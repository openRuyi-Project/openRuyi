# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Digest-JHash
Version:        0.10
Release:        %autorelease
Summary:        Perl extension for 32 bit Jenkins Hashing Algorithm
License:        Artistic-2.0
URL:            https://metacpan.org/release/Digest-JHash
#!RemoteAsset:  sha256:c746cf0a861a004090263cd54d7728d0c7595a0cf90cbbfd8409b396ee3b0063
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Digest-JHash-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)

%description
The Digest::JHash module allows you to use the fast JHash hashing algorithm
developed by Bob Jenkins from within Perl programs. The algorithm takes as
input a message of arbitrary length and produces as output a 32-bit
"message digest" of the input in the form of an unsigned long integer.

%prep
%setup -q -n Digest-JHash-%{version}

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
