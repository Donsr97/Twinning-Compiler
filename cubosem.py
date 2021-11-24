cubosem = {
	'+' : {
		'int' : {
			'int' 	: 'int',
			'float' : 'float',
			'bool' 	: 'error',
			'char' 	: 'error',
		},
		'char' : {
			'int' 	: 'error',
			'float' : 'error',
			'bool' 	: 'error',
			'char' 	: 'error',
		},
		'bool' : {
			'int' 	: 'error',
			'float' : 'error',
			'bool' 	: 'error',
			'char' 	: 'error',
		},
		'float' : {
			'int' : 'float',
			'float' : 'float',
			'bool' : 'error',
			'char' : 'error',
		}
	},

	'-' : {
		'int' : {
			'int' 	: 'int',
			'char' 	: 'error',
			'bool' 	: 'error',
			'float' : 'float',
		},
		'char' : {
			'int' 	: 'error',
			'char' 	: 'error',
			'bool' 	: 'error',
			'float' : 'error',
		},
		'bool' : {
			'int' 	: 'error',
			'char' 	: 'error',
			'bool' 	: 'error',
			'float' : 'error',
		},
		'float' : {
			'int' : 'float',
			'float' : 'float',
			'char' : 'error',
			'bool' : 'error'
		}
	},

	'*' : {
		'int' : {
			'int' 	: 'int',
			'float' : 'float',
			'bool' 	: 'error',
			'char' 	: 'error'
		},
		'char' : {
			'int' 	: 'error',
			'float' : 'error',
			'bool' 	: 'error',
			'char' 	: 'error'
		},
		'bool' : {
			'int' 	: 'error',
			'float' : 'error',
			'bool' 	: 'error',
			'char' 	: 'error'
		},
		'float' : {
			'int' 	: 'float',
			'float' : 'float',
			'bool' 	: 'error',
			'char' 	: 'error',

		}
	},

	'/' : {
		'int' : {
			'int' 	: 'int',
			'float' : 'float',
			'bool' 	: 'error',
			'char' 	: 'error'
		},
		'char' : {
			'int' 	: 'error',
			'float' : 'error',
			'bool' 	: 'error',
			'char' 	: 'error'
		},
		'bool' : {
			'int' 	: 'error',
			'float' : 'error',
			'bool' 	: 'error',
			'char' 	: 'error'
		},
		'float' : {
			'int' 	: 'float',
			'float' : 'float',
			'bool' 	: 'error',
			'char' 	: 'error'
		}
	},

	'=' : {
		'int' : {
			'int' : 'int',
			'float' : 'int',
			'bool' : 'error',
			'char' : 'error'
		},
		'float' : {
			'int' : 'float',
			'float' : 'float',
			'bool' : 'error',
			'char' : 'error'
		},
		'bool' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'bool',
			'char' : 'error'
		},
		'char' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'char'
		}
	},

	'==' : {
			'int' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'error',
				'char' : 'error'
			},
			'float' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'bop',
				'char' : 'error'
			},
			'bool' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'bool',
				'char' : 'error'
			},
			'char' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'bool'
			}
		},

	'!=' : {
			'int' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'error',
				'char' : 'error'
			},
			'float' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'bop',
				'char' : 'error'
			},
			'bool' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'bool',
				'char' : 'error'
			},
			'char' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'bool'
			}
		},

	'<' : {
			'int' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'error',
				'char' : 'error',
				'string' : 'error'
			},
			'float' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'bop',
				'char' : 'error',
				'string' : 'error'
			},
			'bool' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'bool',
				'char' : 'error'
			},
			'char' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'bool'
			}
		},

	'>' : {
			'int' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'error',
				'char' : 'error'
			},
			'float' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'bop',
				'char' : 'error'
			},
			'bool' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'bool',
				'char' : 'error'
			},
			'char' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'bool'
			}
		},

	'<=' : {
			'int' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'error',
				'char' : 'error'
			},
			'float' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'bop',
				'char' : 'error'
			},
			'bool' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'bool',
				'char' : 'error'
			},
			'char' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'bool'
			}
		},

	'>=' : {
			'int' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'error',
				'char' : 'error'
			},
			'float' : {
				'int' : 'bool',
				'float' : 'bool',
				'bool' : 'bop',
				'char' : 'error'
			},
			'bool' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'bool',
				'char' : 'error'
			},
			'char' : {
				'int' : 'error',
				'float' : 'error',
				'bool' : 'error',
				'char' : 'bool'
			}
		},

	'&' : {
		'int' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'error'
		},
		'char' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'error'
		},
		'bool' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'bool',
			'char' : 'error'
		},
		'float' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'error'
		}
	},

	'|' : {
		'int' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'error'
		},
		'char' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'error'
		},
		'bool' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'bool',
			'char' : 'error'
		},
		'float' : {
			'int' : 'error',
			'float' : 'error',
			'bool' : 'error',
			'char' : 'error'
		}
	},

}

cubosemCont = {
	'++' : {
			'int' : 'int',
			'float' : 'float',
			'bool' : 'error',
			'char' : 'error'
		},

	'--' : {
			'int' : 'int',
			'float' : 'float',
			'bool' : 'error',
			'char' : 'error'
		}
	}

def CuboSemRes(operacion, izq, der):
	return cubosem[operacion][izq][der]

def CuboSemContRes(operador, var1):
	return cubosemCont[operador][var1]
