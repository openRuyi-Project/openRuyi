# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Config-Perl-V
Version:        0.39
Release:        %autorelease
Summary:        Structured data retrieval of perl -V output
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Config-Perl-V
#!RemoteAsset:  sha256:a83e8e28f416d9a3f70afee8a37cb0ac1515cbf941c677e9f1f97b643bffedab
Source0:        https://www.cpan.org/authors/id/H/HM/HMBRAND/Config-Perl-V-%{version}.tgz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)

# don't use cpan2spec's description.
%description
The command "perl -V" will return you an excerpt from the %Config::Config
hash combined with the output of "perl -V" that is not stored inside the hash,
but only available to the perl binary itself. This package provides Perl
module that will return you the output of "perl -V" in a structure.

%files -f %{name}.files
%doc Changelog CONTRIBUTING.md README SECURITY.md

%changelog
%autochangelog
