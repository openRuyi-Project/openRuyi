# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Error
Version:        0.17030
Release:        %autorelease
Summary:        Error/exception handling in an OO-ish way
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Error
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/S/SH/SHLOMIF/Error-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
The Error package provides two interfaces. Firstly Error provides a
procedural interface to exception handling. Secondly Error is a base class
for errors/exceptions that can either be thrown, for subsequent catch, or
can simply be recorded.

%prep
%setup -q -n Error-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog Changes examples README scripts weaver.ini

%changelog
%autochangelog
