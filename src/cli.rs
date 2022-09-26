use std::path::PathBuf;

use clap::{Args, Parser, Subcommand};

#[derive(Parser, Debug)]
#[clap(name = "nala-rs")]
#[clap(author = "Blake Lee <blake@volian.org>")]
#[clap(version = "0.1.0")]
#[clap(about = "Commandline front-end for libapt-pkg", long_about = None)]
pub struct NalaParser {
	/// Print license information
	#[clap(global = true, short, long, action)]
	pub license: bool,

	/// Disable scrolling text and print extra information
	#[clap(global = true, short, long, action)]
	pub verbose: bool,

	/// Print debug statements for solving issues
	#[clap(global = true, short, long, action)]
	pub debug: bool,

	/// Specify a different configuration file
	#[clap(short, long, value_parser, value_name = "FILE")]
	pub config: Option<PathBuf>,

	#[clap(subcommand)]
	pub command: Option<Commands>,
}

#[derive(Subcommand, Debug)]
pub enum Commands {
	List(List),
	Search(Search),
}

#[derive(Args, Debug)]
pub struct List {
	/// Package names to search
	#[clap(required = false)]
	pub pkg_names: Vec<String>,

	/// Print the full description of each package
	#[clap(long, action)]
	pub description: bool,

	/// Print the summary of each package
	#[clap(long, action)]
	pub summary: bool,

	/// Show all versions of a package
	#[clap(short, long, action)]
	pub all_versions: bool,

	/// Only include packages that are installed
	#[clap(short, long, action)]
	pub installed: bool,

	/// Only include packages explicitly installed with Nala
	#[clap(short = 'N', long, action)]
	pub nala_installed: bool,

	/// Only include packages that are upgradable
	#[clap(short, long, action)]
	pub upgradable: bool,

	/// Only include virtual packages
	#[clap(short = 'V', long, action)]
	pub r#virtual: bool,
}

#[derive(Args, Debug)]
pub struct Search {
	/// Search is basically list but with an added restriction
	/// by allowing only searching pkg names
	#[clap(long, action)]
	pub names: bool,

	#[clap(flatten)]
	pub list_args: List,
}
