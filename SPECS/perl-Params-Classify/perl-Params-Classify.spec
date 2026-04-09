# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Params-Classify
Version:        0.015
Release:        %autorelease
Summary:        Argument type classification
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Params-Classify
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/Z/ZE/ZEFRAM/Params-Classify-%{version}.tar.gz

BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.1
BuildRequires:  perl(Devel::CallChecker) >= 0.003
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util) >= 1.01
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)

Requires:       perl(Devel::CallChecker) >= 0.003
Requires:       perl(Scalar::Util) >= 1.01

%description
This module provides various type-testing functions. These are intended
for functions that, unlike most Perl code, care what type of data they
are operating on. For example, some functions wish to behave
differently depending on the type of their arguments (like overloaded
functions in C++).

%prep
%setup -q -n Params-Classify-%{version}

%build
perl Build.PL --installdirs=vendor optimize="%{optflags}"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
