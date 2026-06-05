# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Parse-RecDescent
Version:        1.967015
Release:        %autorelease
Summary:        Generate Recursive-Descent Parsers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Parse-RecDescent
#!RemoteAsset:  sha256:1943336a4cb54f1788a733f0827c0c55db4310d5eae15e542639c9dd85656e37
Source0:        https://www.cpan.org/authors/id/J/JT/JTBRAUN/Parse-RecDescent-%{version}.tar.gz
BuildSystem:    perlbuild

BuildOption(build):  --installdirs=vendor optimize="%{optflags}"
BuildOption(install):  --destdir=%{buildroot} --create_packlist=0

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.5702
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Balanced) >= 1.95

Requires:       perl(Text::Balanced) >= 1.95

%description
Overview

%files -f %{name}.files
%doc Changes README ToDo

%changelog
%autochangelog
