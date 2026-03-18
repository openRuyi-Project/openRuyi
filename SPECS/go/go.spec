# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# code.google.com/p/go/issues/detail?id=5238
%global debug_package %{nil}

%bcond bootstrap 1

%if %{with bootstrap}
%bcond race 0
%bcond cshared 0
%else
%bcond race 0
%bcond shared 0
%endif

%ifarch x86_64
%global gohostarch amd64
%endif
%ifarch riscv64
%global gohostarch riscv64
%endif

# we are shipping the full contents of src in the data subpackage, which
# contains binary-like things (ELF data for tests, etc)
%global _binaries_in_noarch_packages_terminate_build 0

# Do not check any files in doc or src for requires
%global __requires_exclude_from ^(%{_datadir}|/usr/lib)/%{name}/(doc|src)/.*$

# Don't alter timestamps of especially the .a files (or else go will rebuild later)
# Actually, don't strip at all since we are not even building debug packages and this corrupts the dwarf testdata
%global __strip /bin/true

# rpmbuild magic to keep from having meta dependency on libc.so.6
%define _use_internal_dependency_generator 0
%define __find_requires %{nil}
%global __spec_install_post /usr/lib/rpm/check-rpaths   /usr/lib/rpm/check-buildroot  \
  /usr/lib/rpm/brp-compress

Name:           go
Version:        1.25.8
Release:        %autorelease
Summary:        The Go Programming Language toolchain
License:        BSD-3-Clause
URL:            https://go.dev/
VCS:            git:https://github.com/golang/go
#!RemoteAsset
Source0:        https://go.dev/dl/%{name}%{version}.src.tar.gz
%if %{with bootstrap}
#!RemoteAsset
Source1:        https://go.dev/dl/%{name}%{version}.linux-%{gohostarch}.tar.gz
%endif

# https://go-review.googlesource.com/c/go/+/732560
Patch1:	0001-crypto-sha1-provide-optimised-assembly-for-riscv64.patch

# Bootstrap from a pre-existing Go compiler.
%if %{without bootstrap}
BuildRequires:  go
%endif
BuildRequires:  gcc, make

Provides:       golang = %{version}-%{release}
Recommends:     %{name}-cshared = %{version}-%{release}
Requires:       glibc

%description
The Go Programming Language. This package contains the compiler, tools,
and standard library sources necessary for developing Go applications.

%package        doc
Summary:        Go language documentation
BuildArch:      noarch

%description    doc
Contains the complete offline HTML documentation for the Go language.

%package        tests
Summary:        Go toolchain and standard library test suite
BuildArch:      noarch
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tests
Contains the upstream test suite for Go, useful for toolchain validation.

%if %{with shared}
%package        shared
Summary:        shared libraries for the Go standard library

%description    shared
Contains shared-object (.so) versions of the Go standard library.
%endif

%if %{with race}
%package        race
Summary:        Race detector enabled standard library for Go
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    race
Contains the Go standard library pre-compiled with race detector support.
%endif

%prep
%autosetup -p1 -n %{name}

%if %{with bootstrap}
mkdir -p %{_builddir}/%{name}-bootstrap
tar -xf %{SOURCE1} -C %{_builddir}/%{name}-bootstrap --strip-components=1
%endif

%build
export GOROOT_FINAL=%{_libdir}/%{name}
export GOHOSTOS=linux
export GOHOSTARCH=%{gohostarch}
%if %{with bootstrap}
export GOROOT_BOOTSTRAP=%{_builddir}/%{name}-bootstrap
%else
export GOROOT_BOOTSTRAP=%{_libdir}/golang
%endif

pushd src
./make.bash -v
popd

%if %{with shared}
# Building cshared standard library
GOROOT=$(pwd) PATH=$(pwd)/bin:$PATH go install -buildmode=shared -v std
%endif
%if %{with race}
# Building race-enabled standard library
GOROOT=$(pwd) PATH=$(pwd)/bin:$PATH go install -race -v std
%endif

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/%{name}/

# Install all built artifacts. We will sort them into packages in %files.
cp -a api bin pkg src misc test VERSION %{buildroot}%{_libdir}/%{name}/
cp -a doc %{buildroot}%{_datadir}/

# Link the main binaries into /usr/bin
ln -sf %{_libdir}/%{name}/bin/go %{buildroot}%{_bindir}/go
ln -sf %{_libdir}/%{name}/bin/gofmt %{buildroot}%{_bindir}/gofmt

# Remove unnecessary bootstrap artifacts
rm -rf %{buildroot}%{_libdir}/%{name}/pkg/bootstrap

# Move cshared libraries to their final destination
install -d %{buildroot}%{_libdir}/golang

%if %{with shared}
mv %{buildroot}%{_libdir}/%{name}/pkg/linux_%{gohostarch}_dynlink/*.so %{buildroot}%{_libdir}/golang/
%endif

%check
# Run the test suite, but its files will be in the -devel package.
export GOROOT_FINAL=%{_libdir}/%{name}/
export PATH="%{buildroot}%{_libdir}/%{name}/bin:$PATH"
export GOTOOLDIR="%{buildroot}%{_libdir}/%{name}/pkg/tool/linux_%{gohostarch}"
export GO_TEST_TIMEOUT_SCALE=20
pushd src
./run.bash --no-rebuild -v -v -v -k -run "!(cmd/cgo/internal/testsanitizers|syscall)"
popd

%files
%license LICENSE
%doc README.md
%{_bindir}/go
%{_bindir}/gofmt
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/api
%{_libdir}/%{name}/bin
%{_libdir}/%{name}/pkg
%{_libdir}/%{name}/src
%{_libdir}/%{name}/misc
%{_libdir}/%{name}/VERSION
%exclude %{_libdir}/%{name}/test
%exclude %{_libdir}/%{name}/src/**/*_test.go
%exclude %{_libdir}/%{name}/src/**/testdata
%if %{with cshared}
%exclude %{_libdir}/%{name}/pkg/linux_%{gohostarch}_dynlink
%endif
%if %{with race}
%exclude %{_libdir}/%{name}/pkg/linux_%{gohostarch}_race
%endif

%files doc
%{_datadir}/*

%files tests
%{_libdir}/%{name}/test
%{_libdir}/%{name}/src/**/*_test.go
%dir %{_libdir}/%{name}/src/**/testdata

%if %{with shared}
%files shared
%{_libdir}/golang/*.so
%{_libdir}/%{name}/pkg/linux_%{gohostarch}_dynlink/
%endif

%if %{with race}
%files race
%{_libdir}/%{name}/pkg/linux_%{gohostarch}_race/
%endif

%changelog
%{?autochangelog}
