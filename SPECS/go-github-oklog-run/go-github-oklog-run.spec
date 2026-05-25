# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           run
%define go_import_path  github.com/oklog/run

Name:           go-github-oklog-run
Version:        1.2.0
Release:        %autorelease
Summary:        A universal mechanism to manage goroutine lifecycles
License:        Apache-2.0
URL:            https://github.com/oklog/run
#!RemoteAsset:  sha256:a27d16ea647cef098c45404806ef087a84f18adce6ea637f81839009280068bc
Source0:        https://github.com/oklog/run/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n run-1.2.0

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/oklog/run) = %{version}


%description
run

[Image: GoDoc] (https://godoc.org/github.com/oklog/run?status.svg)
(https://godoc.org/github.com/oklog/run) [Image: test]
(https://github.com/oklog/run/actions/workflows/test.yaml/badge.
svg?branch=main&event=push)
(https://github.com/oklog/run/actions/workflows/test.yaml) [Image: Go
Report Card] (https://goreportcard.com/badge/github.com/oklog/run)
(https://goreportcard.com/report/github.com/oklog/run) [Image: Apache 2
licensed] (https://img.shields.io/badge/license-Apache2-blue.svg)
(https://raw.githubusercontent.com/oklog/run/master/LICENSE)

run.Group is a universal mechanism to manage goroutine lifecycles.

Create a zero-value run.Group, and then add actors to it. Actors are
defined as a pair of functions: an **execute** function, which should
run synchronously; and an **interrupt** function, which, when invoked,
should cause the execute function to return. Finally, invoke Run, which
concurrently runs all of the actors, waits until the first actor exits,
invokes the interrupt functions, and finally returns control to the
caller only once all actors have returned. This general-purpose API
allows callers to model pretty much any runnable task, and achieve well-
defined lifecycle semantics for the group.

run.Group was written to manage component lifecycles in func main for OK
Log (https://github.com/oklog/oklog). But it's useful in any
circumstance where you need to orchestrate multiple goroutines as a unit
whole. Click here (https://www.youtube.com/watch?v=LHe1Cb_Ud_M&t=15m45s)
to see a video of a talk where run.Group is described.

Examples

context.Context

  ctx, cancel := context.WithCancel(context.Background())
  g.Add(func() error {
  	return myProcess(ctx, ...)
  }, func(error) {
  	cancel()
  })

net.Listener

  ln, _ := net.Listen("tcp", ":8080")
  g.Add(func() error {
  	return http.Serve(ln, nil)
  }, func(error) {
  	ln.Close()
  })

io.ReadCloser

  var conn io.ReadCloser = ...
  g.Add(func() error {
  	s := bufio.NewScanner(conn)
  	for s.Scan() {
  		println(s.Text())
  	}
  	return s.Err()
  }, func(error) {
  	conn.Close()
  })

http.Server graceful Shutdown

  httpServer := &http.Server{
  	Addr:    "localhost:8080",
  	Handler: ...,
  }
  g.Add(func() error {
  	return httpServer.ListenAndServe()
  }, func(error) {
  	ctx, cancel := context.WithTimeout(context.TODO(), 3*time.Second)
  	defer cancel()
  	httpServer.Shutdown(ctx)
  })

Comparisons

Package run is somewhat similar to package errgroup
(https://godoc.org/golang.org/x/sync/errgroup), except it doesn't
require actor goroutines to understand context semantics.

It's somewhat similar to package tomb.v1
(https://godoc.org/gopkg.in/tomb.v1) or tomb.v2
(https://godoc.org/gopkg.in/tomb.v2), except it has a much smaller API
surface, delegating e.g. staged shutdown of goroutines to the caller.


%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
