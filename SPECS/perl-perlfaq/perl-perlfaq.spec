# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-perlfaq
Version:        5.20250619
Release:        %autorelease
Summary:        Frequently asked questions about Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/perlfaq
#!RemoteAsset:  sha256:eed03a887f21e2bede71c07645357a26cabde487365ac17fa3366baaeb0ea8d6
Source0:        https://www.cpan.org/authors/id/E/ET/ETHER/perlfaq-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)

%description
The perlfaq comprises several documents that answer the most commonly asked
questions about Perl and Perl programming. It's divided by topic into nine
major sections outlined in this document.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
