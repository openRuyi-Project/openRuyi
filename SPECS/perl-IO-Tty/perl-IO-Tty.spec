# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IO-Tty
Version:        1.31
Release:        %autorelease
Summary:        Pseudo ttys and constants
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-Tty
#!RemoteAsset:  sha256:d597af221628571cbecf35b44520148c44798dfc8a9867774e60453f79d25ff7
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/IO-Tty-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

%description
IO::Tty provides pseudo terminal support and terminal related constants for
Perl programs.

%files -f %{name}.files
%doc AI_POLICY.md ChangeLog CONTRIBUTING.md README.md SECURITY.md try
%license LICENSE

%changelog
%autochangelog
