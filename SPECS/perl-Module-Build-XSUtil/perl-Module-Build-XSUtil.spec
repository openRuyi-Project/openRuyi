# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Module-Build-XSUtil
Version:        0.19
Release:        %autorelease
Summary:        Module::Build class for building XS modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Module-Build-XSUtil
#!RemoteAsset:  sha256:9063b3c346edeb422807ffe49ffb23038c4f900d4a77b845ce4b53d97bf29400
Source0:        https://cpan.metacpan.org/authors/id/H/HI/HIDEAKIO/Module-Build-XSUtil-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.4005
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Cwd::Guard)
BuildRequires:  perl(Devel::CheckCompiler)
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Copy::Recursive::Reduced) >= 0.002
BuildRequires:  perl(Test::More) >= 0.98

Requires:       perl(Devel::CheckCompiler)
Requires:       perl(Devel::PPPort)
Requires:       perl(ExtUtils::CBuilder)

%description
Module::Build::XSUtil extends Module::Build with helpers for XS module
configuration and compilation.

%files -f %{name}.files
%doc Changes README.md
%license LICENSE

%changelog
%autochangelog
