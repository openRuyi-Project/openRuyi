# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-AnyEvent
Version:        7.17
Release:        %autorelease
Summary:        Framework for multiple event loops
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/AnyEvent
#!RemoteAsset:  sha256:50beea689c098fe4aaeb83806c40b9fe7f946d5769acf99f849f099091a4b985
Source0:        https://www.cpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl-devel
BuildRequires:  perl(Canary::Stability)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)

%description
AnyEvent provides a common API for multiple Perl event loops.

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
