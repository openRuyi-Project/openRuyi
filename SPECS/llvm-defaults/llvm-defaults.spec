# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

# This package provides default/unversioned symlinks for LLVM 22 tools
# It creates symlinks like /usr/bin/clang -> clang-22

%global maj_ver 22

Name:           llvm-defaults
Version:        %{maj_ver}
Release:        %{autorelease}
Summary:        Default symlinks for LLVM %{maj_ver} tools
License:        Apache-2.0 WITH LLVM-exception OR NCSA
URL:            http://llvm.org

BuildRequires:  llvm%{maj_ver}
BuildRequires:  clang%{maj_ver}
BuildRequires:  clang%{maj_ver}-tools-extra
BuildRequires:  clang%{maj_ver}-analyzer
BuildRequires:  llvm-bolt%{maj_ver}
BuildRequires:  lld%{maj_ver}
BuildRequires:  lldb%{maj_ver}

%description
This package provides default unversioned symlinks for LLVM %{maj_ver} tools,
creating symlinks like /usr/bin/clang -> clang-22, /usr/bin/flang -> flang-22, etc.

# ============================================================================
# llvm subpackage
# ============================================================================
%package     -n llvm
Summary:        Default symlinks for LLVM tools
Requires:       llvm%{maj_ver} > %{maj_ver}

%description -n llvm
This package provides default unversioned symlinks for LLVM %{maj_ver} tools,
creating symlinks like /usr/bin/llc -> llc-22, /usr/bin/opt -> opt-22, etc.

# ============================================================================
# clang subpackage
# ============================================================================
%package     -n clang
Summary:        Default symlinks for clang
Requires:       clang%{maj_ver} > %{maj_ver}

%description -n clang
This package provides default unversioned symlinks for clang %{maj_ver},
creating symlinks like /usr/bin/clang -> clang-22, /usr/bin/clang++ -> clang++-22, etc.

# ============================================================================
# clang-tools-extra subpackage
# ============================================================================
%package     -n clang-tools-extra
Summary:        Default symlinks for extra clang tools
Requires:       clang%{maj_ver}-tools-extra > %{maj_ver}

%description -n clang-tools-extra
This package provides default unversioned symlinks for extra clang tools %{maj_ver}.

# ============================================================================
# clang-analyzer subpackage
# ============================================================================
%package     -n clang-analyzer
Summary:        Default symlinks for clang static analyzer
Requires:       clang%{maj_ver}-analyzer > %{maj_ver}

%description -n clang-analyzer
This package provides default unversioned symlinks for clang static analyzer %{maj_ver}.

# ============================================================================
# flang subpackage
# ============================================================================
%package     -n flang
Summary:        Default symlinks for flang (Fortran frontend)
Requires:       llvm%{maj_ver} > %{maj_ver}

%description -n flang
This package provides default unversioned symlinks for flang %{maj_ver},
the Fortran frontend for LLVM.

# ============================================================================
# llvm-bolt subpackage
# ============================================================================
%package     -n llvm-bolt
Summary:        Default symlinks for LLVM BOLT (Binary Optimization and Layout Tool)
Requires:       llvm-bolt%{maj_ver} > %{maj_ver}

%description -n llvm-bolt
This package provides default unversioned symlinks for LLVM BOLT %{maj_ver},
a post-link optimizer developed to speed up large applications.

# ============================================================================
# lld subpackage
# ============================================================================
%package     -n lld
Summary:        Default symlinks for LLVM lld linker
Requires:       lld%{maj_ver} > %{maj_ver}

%description -n lld
This package provides default unversioned symlinks for LLVM lld linker %{maj_ver}.

# ============================================================================
# lldb subpackage
# ============================================================================
%package     -n lldb
Summary:        Default symlinks for LLVM lldb debugger
Requires:       lldb%{maj_ver} > %{maj_ver}

%description -n lldb
This package provides default unversioned symlinks for LLVM lldb debugger %{maj_ver}.

# ============================================================================
# Install section - create symlinks
# ============================================================================
%install
mkdir -p %{buildroot}%{_bindir}

# LLVM tools symlinks
ln -sf llc-%{maj_ver} %{buildroot}%{_bindir}/llc
ln -sf opt-%{maj_ver} %{buildroot}%{_bindir}/opt
ln -sf llvm-config-%{maj_ver} %{buildroot}%{_bindir}/llvm-config
ln -sf llvm-ar-%{maj_ver} %{buildroot}%{_bindir}/llvm-ar
ln -sf llvm-nm-%{maj_ver} %{buildroot}%{_bindir}/llvm-nm
ln -sf llvm-objcopy-%{maj_ver} %{buildroot}%{_bindir}/llvm-objcopy
ln -sf llvm-objdump-%{maj_ver} %{buildroot}%{_bindir}/llvm-objdump
ln -sf llvm-ranlib-%{maj_ver} %{buildroot}%{_bindir}/llvm-ranlib
ln -sf llvm-strip-%{maj_ver} %{buildroot}%{_bindir}/llvm-strip
ln -sf llvm-as-%{maj_ver} %{buildroot}%{_bindir}/llvm-as
ln -sf llvm-dis-%{maj_ver} %{buildroot}%{_bindir}/llvm-dis
ln -sf llvm-link-%{maj_ver} %{buildroot}%{_bindir}/llvm-link
ln -sf llvm-profdata-%{maj_ver} %{buildroot}%{_bindir}/llvm-profdata
ln -sf llvm-symbolizer-%{maj_ver} %{buildroot}%{_bindir}/llvm-symbolizer
ln -sf llvm-cov-%{maj_ver} %{buildroot}%{_bindir}/llvm-cov
ln -sf llvm-dwarfdump-%{maj_ver} %{buildroot}%{_bindir}/llvm-dwarfdump
ln -sf llvm-dwp-%{maj_ver} %{buildroot}%{_bindir}/llvm-dwp
ln -sf llvm-bcanalyzer-%{maj_ver} %{buildroot}%{_bindir}/llvm-bcanalyzer
ln -sf llvm-readelf-%{maj_ver} %{buildroot}%{_bindir}/llvm-readelf
ln -sf llvm-readobj-%{maj_ver} %{buildroot}%{_bindir}/llvm-readobj
ln -sf llvm-size-%{maj_ver} %{buildroot}%{_bindir}/llvm-size
ln -sf llvm-strings-%{maj_ver} %{buildroot}%{_bindir}/llvm-strings
ln -sf llvm-addr2line-%{maj_ver} %{buildroot}%{_bindir}/llvm-addr2line
ln -sf dsymutil-%{maj_ver} %{buildroot}%{_bindir}/dsymutil
ln -sf FileCheck-%{maj_ver} %{buildroot}%{_bindir}/FileCheck
ln -sf lli-%{maj_ver} %{buildroot}%{_bindir}/lli
ln -sf llvm-lto-%{maj_ver} %{buildroot}%{_bindir}/llvm-lto
ln -sf llvm-lto2-%{maj_ver} %{buildroot}%{_bindir}/llvm-lto2
ln -sf llvm-mc-%{maj_ver} %{buildroot}%{_bindir}/llvm-mc
ln -sf llvm-mca-%{maj_ver} %{buildroot}%{_bindir}/llvm-mca

# clang symlinks
ln -sf clang-%{maj_ver} %{buildroot}%{_bindir}/clang
ln -sf clang++-%{maj_ver} %{buildroot}%{_bindir}/clang++
ln -sf clang-cl-%{maj_ver} %{buildroot}%{_bindir}/clang-cl
ln -sf clang-cpp-%{maj_ver} %{buildroot}%{_bindir}/clang-cpp
ln -sf clang-scan-deps-%{maj_ver} %{buildroot}%{_bindir}/clang-scan-deps

# clang-tools-extra symlinks
ln -sf clang-format-%{maj_ver} %{buildroot}%{_bindir}/clang-format
ln -sf clang-tidy-%{maj_ver} %{buildroot}%{_bindir}/clang-tidy
ln -sf clangd-%{maj_ver} %{buildroot}%{_bindir}/clangd
ln -sf clang-apply-replacements-%{maj_ver} %{buildroot}%{_bindir}/clang-apply-replacements
ln -sf clang-change-namespace-%{maj_ver} %{buildroot}%{_bindir}/clang-change-namespace
ln -sf clang-check-%{maj_ver} %{buildroot}%{_bindir}/clang-check
ln -sf clang-doc-%{maj_ver} %{buildroot}%{_bindir}/clang-doc
ln -sf clang-include-cleaner-%{maj_ver} %{buildroot}%{_bindir}/clang-include-cleaner
ln -sf clang-include-fixer-%{maj_ver} %{buildroot}%{_bindir}/clang-include-fixer
ln -sf clang-move-%{maj_ver} %{buildroot}%{_bindir}/clang-move
ln -sf clang-offload-bundler-%{maj_ver} %{buildroot}%{_bindir}/clang-offload-bundler
ln -sf clang-offload-packager-%{maj_ver} %{buildroot}%{_bindir}/clang-offload-packager
ln -sf clang-query-%{maj_ver} %{buildroot}%{_bindir}/clang-query
ln -sf clang-refactor-%{maj_ver} %{buildroot}%{_bindir}/clang-refactor
ln -sf clang-reorder-fields-%{maj_ver} %{buildroot}%{_bindir}/clang-reorder-fields
ln -sf clang-repl-%{maj_ver} %{buildroot}%{_bindir}/clang-repl
ln -sf git-clang-format-%{maj_ver} %{buildroot}%{_bindir}/git-clang-format
ln -sf clang-format-diff-%{maj_ver} %{buildroot}%{_bindir}/clang-format-diff
ln -sf run-clang-tidy-%{maj_ver} %{buildroot}%{_bindir}/run-clang-tidy

# clang-analyzer symlinks
ln -sf scan-view-%{maj_ver} %{buildroot}%{_bindir}/scan-view
ln -sf scan-build-%{maj_ver} %{buildroot}%{_bindir}/scan-build

# flang symlinks
ln -sf flang-%{maj_ver} %{buildroot}%{_bindir}/flang
ln -sf flang-new-%{maj_ver} %{buildroot}%{_bindir}/flang-new
ln -sf f18-%{maj_ver} %{buildroot}%{_bindir}/f18
ln -sf bbc-%{maj_ver} %{buildroot}%{_bindir}/bbc
ln -sf fir-opt-%{maj_ver} %{buildroot}%{_bindir}/fir-opt
ln -sf tco-%{maj_ver} %{buildroot}%{_bindir}/tco

# bolt symlinks
ln -sf llvm-bolt-%{maj_ver} %{buildroot}%{_bindir}/llvm-bolt
ln -sf llvm-boltdiff-%{maj_ver} %{buildroot}%{_bindir}/llvm-boltdiff
ln -sf llvm-bolt-binary-analysis-%{maj_ver} %{buildroot}%{_bindir}/llvm-bolt-binary-analysis
ln -sf llvm-bolt-heatmap-%{maj_ver} %{buildroot}%{_bindir}/llvm-bolt-heatmap
ln -sf merge-fdata-%{maj_ver} %{buildroot}%{_bindir}/merge-fdata
ln -sf perf2bolt-%{maj_ver} %{buildroot}%{_bindir}/perf2bolt

# lld symlinks
ln -sf lld-%{maj_ver} %{buildroot}%{_bindir}/lld
ln -sf lld-link-%{maj_ver} %{buildroot}%{_bindir}/lld-link
ln -sf ld.lld-%{maj_ver} %{buildroot}%{_bindir}/ld.lld
ln -sf ld64.lld-%{maj_ver} %{buildroot}%{_bindir}/ld64.lld
ln -sf wasm-ld-%{maj_ver} %{buildroot}%{_bindir}/wasm-ld

# lldb symlinks
ln -sf lldb-%{maj_ver} %{buildroot}%{_bindir}/lldb
ln -sf lldb-argdumper-%{maj_ver} %{buildroot}%{_bindir}/lldb-argdumper
ln -sf lldb-dap-%{maj_ver} %{buildroot}%{_bindir}/lldb-dap
ln -sf lldb-instr-%{maj_ver} %{buildroot}%{_bindir}/lldb-instr
ln -sf lldb-server-%{maj_ver} %{buildroot}%{_bindir}/lldb-server
ln -sf lldb-mcp-%{maj_ver} %{buildroot}%{_bindir}/lldb-mcp

# ============================================================================
# Files section
# ============================================================================
%files -n llvm
%{_bindir}/llc
%{_bindir}/opt
%{_bindir}/llvm-config
%{_bindir}/llvm-ar
%{_bindir}/llvm-nm
%{_bindir}/llvm-objcopy
%{_bindir}/llvm-objdump
%{_bindir}/llvm-ranlib
%{_bindir}/llvm-strip
%{_bindir}/llvm-as
%{_bindir}/llvm-dis
%{_bindir}/llvm-link
%{_bindir}/llvm-profdata
%{_bindir}/llvm-symbolizer
%{_bindir}/llvm-cov
%{_bindir}/llvm-dwarfdump
%{_bindir}/llvm-dwp
%{_bindir}/llvm-bcanalyzer
%{_bindir}/llvm-readelf
%{_bindir}/llvm-readobj
%{_bindir}/llvm-size
%{_bindir}/llvm-strings
%{_bindir}/llvm-addr2line
%{_bindir}/dsymutil
%{_bindir}/FileCheck
%{_bindir}/lli
%{_bindir}/llvm-lto
%{_bindir}/llvm-lto2
%{_bindir}/llvm-mc
%{_bindir}/llvm-mca

%files -n clang
%{_bindir}/clang
%{_bindir}/clang++
%{_bindir}/clang-cl
%{_bindir}/clang-cpp
%{_bindir}/clang-scan-deps

%files -n clang-tools-extra
%{_bindir}/clang-format
%{_bindir}/clang-tidy
%{_bindir}/clangd
%{_bindir}/clang-apply-replacements
%{_bindir}/clang-change-namespace
%{_bindir}/clang-check
%{_bindir}/clang-doc
%{_bindir}/clang-include-cleaner
%{_bindir}/clang-include-fixer
%{_bindir}/clang-move
%{_bindir}/clang-offload-bundler
%{_bindir}/clang-offload-packager
%{_bindir}/clang-query
%{_bindir}/clang-refactor
%{_bindir}/clang-reorder-fields
%{_bindir}/clang-repl
%{_bindir}/git-clang-format
%{_bindir}/clang-format-diff
%{_bindir}/run-clang-tidy

%files -n clang-analyzer
%{_bindir}/scan-view
%{_bindir}/scan-build

%files -n flang
%{_bindir}/flang
%{_bindir}/flang-new
%{_bindir}/f18
%{_bindir}/bbc
%{_bindir}/fir-opt
%{_bindir}/tco

%files -n llvm-bolt
%{_bindir}/llvm-bolt
%{_bindir}/llvm-boltdiff
%{_bindir}/llvm-bolt-binary-analysis
%{_bindir}/llvm-bolt-heatmap
%{_bindir}/merge-fdata
%{_bindir}/perf2bolt

%files -n lld
%{_bindir}/lld
%{_bindir}/lld-link
%{_bindir}/ld.lld
%{_bindir}/ld64.lld
%{_bindir}/wasm-ld

%files -n lldb
%{_bindir}/lldb
%{_bindir}/lldb-argdumper
%{_bindir}/lldb-dap
%{_bindir}/lldb-instr
%{_bindir}/lldb-server
%{_bindir}/lldb-mcp

%changelog
%autochangelog

